from PySide2.QtWidgets import QDialog

from germanium_build_monitor.ui.Ui_MainDialog import Ui_Dialog

main_dialog = None


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)

        self.setupUi(self)

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

