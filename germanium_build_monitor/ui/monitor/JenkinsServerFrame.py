from mopyx import render, render_call

from PySide2.QtWidgets import QWidget

from germanium_build_monitor.ui.generated.Ui_JenkinsServerFrame import Ui_Form
from germanium_build_monitor.model.JenkinsServer import JenkinsServer
from germanium_build_monitor.ui.core import clear_layout

from .LoadingJobFrame import LoadingJobFrame
from .JenkinsBuildBranchFrame import JenkinsBuildBranchFrame


class JenkinsServerFrame(QWidget, Ui_Form):
    def __init__(self,
                 server: JenkinsServer) -> None:
        super().__init__()

        self.server = server

        self.setupUi(self)
        self.update_ui()

    @render
    def update_ui(self) -> None:
        @render_call
        def update_server_label() -> None:
            self.server_name_label.setText(f"<b>{self.server.name}</b>")

        @render_call
        def update_branches() -> None:
            print("update branches called")
            not_loaded_jobs = []
            build_branches = []

            clear_layout(self.content)

            for job in self.server.monitored_jobs:
                if job.branches is None:
                    not_loaded_jobs.append(job)
                    continue

                for branch in job.branches:
                    build_branches.append(branch)

            for job in not_loaded_jobs:
                self.content.addWidget(LoadingJobFrame(job))

            build_branches.sort(key=lambda it: it.last_build_timestamp if it.last_build_timestamp else 0,
                                reverse=True)

            # FIXME: sort by last build time
            for branch in build_branches:
                self.content.addWidget(JenkinsBuildBranchFrame(branch))

