from mopyx import model, render

from PySide2.QtWidgets import QDialog, QWidget

from germanium_build_monitor.ui.Ui_AddJobsFromServerDialog import Ui_Dialog
from germanium_build_monitor.model.JenkinsServer import JenkinsServer

from .WidgetSwitcher import WidgetSwitcher
from .LoadingFrame import LoadingFrame
from .SelectJobsFrame import SelectJobsFrame


@model
class ServerDialogModel:
    def __init__(self,
                 server: JenkinsServer):
        self.server: JenkinsServer = server
        self.loaded = False


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

