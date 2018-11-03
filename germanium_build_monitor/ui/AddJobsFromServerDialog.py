from PySide2.QtWidgets import QDialog

from germanium_build_monitor.ui.Ui_AddJobsFromServerDialog import Ui_Dialog


class AddJobsFromServerDialog(QDialog, Ui_Dialog):
    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)

        self.setupUi(self)
