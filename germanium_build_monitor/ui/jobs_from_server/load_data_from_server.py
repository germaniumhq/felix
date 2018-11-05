from typing import Set, Dict

from mopyx import model
import jenkins

from germanium_build_monitor.model.JenkinsServer import JenkinsServer
from germanium_build_monitor.model.JenkinsFolder import JenkinsFolder
from germanium_build_monitor.model.JenkinsJob import JenkinsJob

from germanium_build_monitor.ui.core import ui_thread_call


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

