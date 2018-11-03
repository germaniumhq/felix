from PySide2.QtWidgets import QDialog, QWidget
from mopyx import render

from germanium_build_monitor.ui.Ui_MainDialog import Ui_Dialog
from germanium_build_monitor.model.RootModel import model

from .WidgetSwitcher import WidgetSwitcher

main_dialog = None


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)

        self.setupUi(self)

        self.content = WidgetSwitcher(self.current_view)

        self.update_current_view()

    @render
    def update_current_view(self):
        if not model.servers:
            self.content.set(NewStartFrame())
        else:
            self.content.set(ServersOverviewFrame())

    @staticmethod
    def instance() -> 'MainDialog':
        global main_dialog

        if not main_dialog:
            main_dialog = MainDialog()
            main_dialog.show()

        return main_dialog

    def closeEvent(self, event) -> None:
        event.ignore()
        self.hide()


from .NewStartFrame import NewStartFrame
from .ServersOverviewFrame import ServersOverviewFrame
