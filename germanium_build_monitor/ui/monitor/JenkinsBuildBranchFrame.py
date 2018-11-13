from mopyx import render_call

from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QSize

from germanium_build_monitor.ui.generated.Ui_JenkinsBuildBranchFrame import Ui_Form
from germanium_build_monitor.model.JenkinsJobBranch import JenkinsJobBranch
from germanium_build_monitor.resources.icons import build_status_icon
from germanium_build_monitor.ui.core import clear_layout

from .SingleBuildStatusFrame import SingleBuildStatusFrame


class JenkinsBuildBranchFrame(QWidget, Ui_Form):
    def __init__(self, branch: JenkinsJobBranch) -> None:
        super().__init__()

        self.setupUi(self)

        self.project_name_label.setText(branch.project_name)
        self.branch_name_label.setText(branch.decoded_branch_name)

        @render_call
        def update_status_icon():
            self.status_icon_label.setPixmap(build_status_icon(branch.status).pixmap(QSize(24, 24)))

        @render_call
        def update_last_builds():
            clear_layout(self.previous_builds_container)

            for build in branch.last_builds:
                self.previous_builds_container.addWidget(SingleBuildStatusFrame(build))
