from typing import Optional

from PySide2.QtWidgets import QMainWindow, QWidget

from germanium_build_monitor.ui.Ui_MainWindow import Ui_MainWindow
from germanium_build_monitor.resources import icons

from .NewStartFrame import NewStartFrame


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowIcon(icons.get_icon("favicon.ico"))

        self.add_server_button.setIcon(icons.get_icon("server24.png"))
        self.add_folder_button.setIcon(icons.get_icon("folder24.png"))
        self.add_job_button.setIcon(icons.get_icon("job24.png"))

        self._last_widget: Optional[QWidget] = None

        self.set_current_widget(NewStartFrame())
        self.set_current_widget(NewStartFrame())

    def set_current_widget(self,
                           widget: QWidget) -> None:
        if self._last_widget:
            self.current_view.removeWidget(self._last_widget)
            self._last_widget.close()

        self.current_view.addWidget(NewStartFrame())

        self._last_widget = widget

    def closeEvent(self, event) -> None:
        event.ignore()
        self.hide()

