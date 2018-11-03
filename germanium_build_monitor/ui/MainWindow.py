from typing import Optional

from PySide2.QtWidgets import QMainWindow, QWidget

from mopyx import render

from germanium_build_monitor.ui.Ui_MainWindow import Ui_MainWindow
from germanium_build_monitor.resources import icons
from germanium_build_monitor.model.RootModel import model


main_window = None


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowIcon(icons.get_icon("favicon.ico"))

        self.add_server_button.setIcon(icons.get_icon("server24.png"))
        self.add_server_button.clicked.connect(open_create_jenkins_server_dialog)

        self.add_folder_button.setIcon(icons.get_icon("folder24.png"))

        self.add_job_button.setIcon(icons.get_icon("job24.png"))

        self._last_widget: Optional[QWidget] = None

        self.update_current_view()
        self.update_buttons_status()

    @render
    def update_current_view(self):
        if not model.servers:
            self.set_current_widget(NewStartFrame())
        elif not model.tree_selection:
            self.set_current_widget(NoSelectionFrame())

    @render
    def update_buttons_status(self):
        self.delete_item_button.setEnabled(model.tree_selection is not None)

    def set_current_widget(self,
                           widget: QWidget) -> None:
        if self._last_widget:
            self._last_widget.deleteLater()
            self.current_view.removeWidget(self._last_widget)

        self.current_view.addWidget(widget)
        self._last_widget = widget

    def closeEvent(self, event) -> None:
        event.ignore()
        self.hide()

    @staticmethod
    def instance() -> 'MainWindow':
        global main_window

        if not main_window:
            main_window = MainWindow()
            main_window.show()

        return main_window


from .NewStartFrame import NewStartFrame
from .NoSelectionFrame import NoSelectionFrame

from germanium_build_monitor.actions.new_jenkins_server import open_create_jenkins_server_dialog
