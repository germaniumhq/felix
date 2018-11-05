from typing import Dict, Set
from mopyx import model, render
import jenkins
import threading

from PySide2.QtWidgets import QDialog, QWidget

from germanium_build_monitor.ui.Ui_AddJobsFromServerDialog import Ui_Dialog
from germanium_build_monitor.model.JenkinsServer import JenkinsServer
from germanium_build_monitor.model.JenkinsFolder import JenkinsFolder
from germanium_build_monitor.model.JenkinsJob import JenkinsJob

from .WidgetSwitcher import WidgetSwitcher
from .LoadingFrame import LoadingFrame
from .SelectJobsFrame import SelectJobsFrame
from .core import ui_thread_call


@model
class ServerDialogModel:
    def __init__(self,
                 server: JenkinsServer):
        self.server: JenkinsServer = server
        self.loaded = False


def load_server(model: ServerDialogModel):
    found_urls: Set[str] = set()
    server = model.server

    if server.use_authentication:
        jenkins_server = jenkins.Jenkins(server.url,
                                         username=server.user,
                                         password=server.password)
    else:
        jenkins_server = jenkins.Jenkins(server.url)

    result = jenkins_server.get_all_jobs()

    def process_folder(folder: JenkinsFolder, entry: Dict):
        f = JenkinsFolder(entry['name'])
        folder.folders.append(f)

        for job in entry['jobs']:
            process(f, job)

    def process_job(folder: JenkinsFolder, entry: Dict):
        url: str = entry['url']

        if url in found_urls:
            return

        found_urls.add(url)

        job = JenkinsJob(name=entry['name'],
                         full_name=entry['fullname'],
                         url=url)
        folder.jobs.append(job)

    def process_workflow_job(folder: JenkinsFolder, entry: Dict):
        if "/" not in entry["fullname"] or not isinstance(folder, JenkinsServer):
            process_job(folder, entry)

    def process(folder: JenkinsFolder, entry: Dict):
        if entry["_class"] == "com.cloudbees.hudson.plugins.folder.Folder":
            process_folder(folder, entry)
        elif entry["_class"] == "org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject":
            process_job(folder, entry)
        elif entry["_class"] == "org.jenkinsci.plugins.workflow.job.WorkflowJob":
            process_workflow_job(folder, entry)
        else:
            print(f"Unprocessed: {entry['_class']}")

    @ui_thread_call
    def update_model():
        for entry in result:
            process(server, entry)

        model.loaded = True


class AddJobsFromServerDialog(QDialog, Ui_Dialog):
    def __init__(self,
                 model: JenkinsServer,
                 main_window: QWidget,
                 edit_mode: bool = False,
                 ) -> None:
        super().__init__(main_window)

        self.model = ServerDialogModel(model)
        self.setupUi(self)

        self.content = WidgetSwitcher(self.content_holder)

        self.wire_signals()
        self.update_from_model()
        self.reactive_update_from_model()

        threading.Thread(target=lambda: load_server(self.model)).start()

    def wire_signals(self):
        self.close_button.clicked.connect(self.close)

    def update_from_model(self):
        self.server_name_label.setText(self.model.server.name)

    @render
    def reactive_update_from_model(self):
        self.select_button.setEnabled(self.model.loaded)

        if not self.model.loaded:
            self.content.set(LoadingFrame())
        else:
            self.content.set(SelectJobsFrame(self.model.server))

