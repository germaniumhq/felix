from mopyx import render
from PySide2.QtWidgets import QWidget

from germanium_build_monitor.ui.generated.Ui_ServersOverviewFrame import Ui_Form
from germanium_build_monitor.ui.monitor.JenkinsServerFrame import JenkinsServerFrame
from germanium_build_monitor.model.RootModel import root_model


class ServersOverviewFrame(QWidget, Ui_Form):
    def __init__(self) -> None:
        super().__init__()

        self.setupUi(self)
        self.load_from_model()

    @render
    def load_from_model(self):
        for server in root_model.servers:
            self.content.addWidget(JenkinsServerFrame(server))
