from mopyx import render_call

from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QSize

from germanium_build_monitor.ui.generated.Ui_SingleBuildStatusFrame import Ui_Form

from germanium_build_monitor.model.JenkinsJobBranchBuild import JenkinsJobBranchBuild
from germanium_build_monitor.resources.icons import build_status_icon


class SingleBuildStatusFrame(QWidget, Ui_Form):
    def __init__(self,
                 build: JenkinsJobBranchBuild) -> None:
        super().__init__()

        self.build: JenkinsJobBranchBuild = build

        self.setupUi(self)

        @render_call
        def update_label():
            pixmap = build_status_icon(self.build.status).pixmap(QSize(16, 16))
            self.icon.setPixmap(pixmap)
            self.icon.setToolTip(self.build.name)
