from mopyx import render, action
import threading

from PySide2.QtWidgets import QDialog

from germanium_build_monitor.ui.generated.Ui_AddJobsFromServerDialog import Ui_Dialog

from germanium_build_monitor.model.JenkinsServer import JenkinsServer

from germanium_build_monitor.ui.WidgetSwitcher import WidgetSwitcher
from germanium_build_monitor.ui.LoadingFrame import LoadingFrame
from germanium_build_monitor.ui.ErrorFrame import ErrorFrame

from .SelectJobsFrame import SelectJobsFrame
from .load_data_from_server import load_server, ServerDialogModel


class AddJobsFromServerDialog(QDialog, Ui_Dialog):
    def __init__(self,
                 model: JenkinsServer,
                 main_window: QDialog,
                 edit_mode: bool = False,
                 ) -> None:
        super().__init__(main_window)

        self.model = ServerDialogModel(model)
        self.setupUi(self)

        self.content = WidgetSwitcher(self.content_holder)

        self.wire_signals()
        self.update_from_model()
        self.reactive_update_from_model()
        self.load_content_from_server()

    def wire_signals(self):
        self.close_button.clicked.connect(self.close)

    def update_from_model(self):
        self.server_name_label.setText(self.model.server.name)

    @render
    def reactive_update_from_model(self):
        self.select_button.setEnabled(self.model.loaded)

        if self.model.error:
            self.content.set(ErrorFrame(self.model.error, self.load_content_from_server))
        elif not self.model.loaded:
            self.content.set(LoadingFrame())
        else:
            self.content.set(SelectJobsFrame(self.model.server))

    def load_content_from_server(self):
        @action
        def clear_model():
            self.model.loaded = False
            self.model.error = None

        clear_model()

        threading.Thread(target=lambda: load_server(self.model)).start()

