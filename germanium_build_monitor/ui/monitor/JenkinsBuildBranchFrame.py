from mopyx import render_call
import arrow

from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QSize

from germanium_build_monitor.ui.generated.Ui_JenkinsBuildBranchFrame import Ui_Form
from germanium_build_monitor.model.JenkinsJobBranch import JenkinsJobBranch
from germanium_build_monitor.resources.icons import branch_status_icon
from germanium_build_monitor.ui.core import clear_layout

from .SingleBuildStatusFrame import SingleBuildStatusFrame


class JenkinsBuildBranchFrame(QWidget, Ui_Form):
    def __init__(self, branch: JenkinsJobBranch) -> None:
        super().__init__()

        self.setupUi(self)

        self.project_name_label.setText(branch.project_name)
        self.branch_name_label.setText(branch.decoded_branch_name)

        @render_call
        def update_status_icon() -> None:
            self.status_icon_label.setPixmap(branch_status_icon(branch).pixmap(QSize(24, 24)))

        @render_call
        def update_last_builds() -> None:
            clear_layout(self.previous_builds_container)

            for build in reversed(branch.last_builds):
                self.previous_builds_container.addWidget(SingleBuildStatusFrame(build))

        @render_call
        def update_time() -> None:
            if branch.last_build_timestamp is None:
                self.time_label.setText("<i>not run</i>")
                return

            time = arrow.get(branch.last_build_timestamp / 1000.0).humanize()
            self.time_label.setText(time)
