from PySide2.QtWidgets import QWidget

from germanium_build_monitor.ui.generated.Ui_SingleBuildStatusFrame import Ui_Form

from germanium_build_monitor.model.JenkinsJobBranchBuild import JenkinsJobBranchBuild


class SingleBuildStatusFrame(QWidget, Ui_Form):
    def __init__(self,
                 build: JenkinsJobBranchBuild) -> None:
        super().__init__()

        self.build = build

        self.setupUi(self)
