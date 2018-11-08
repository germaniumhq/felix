from PySide2.QtWidgets import QWidget

from germanium_build_monitor.ui.generated.Ui_JenkinsBuildBranchFrame import Ui_Form
from germanium_build_monitor.model.JenkinsJobBranch import JenkinsJobBranch


class JenkinsBuildBranchFrame(QWidget, Ui_Form):
    def __init__(self, branch: JenkinsJobBranch) -> None:
        super().__init__()

        self.setupUi(self)

        self.project_name_label.setText(branch.project_name)
        self.branch_name_label.setText(branch.decoded_branch_name)
        self.build_status_label.setText(branch.status.value)
