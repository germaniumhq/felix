from PySide2.QtWidgets import QWidget

from germanium_build_monitor.ui.Ui_ServersOverviewFrame import Ui_Form


class ServersOverviewFrame(QWidget, Ui_Form):
    def __init__(self, *args, **kw) -> None:
        super().__init__(*args, **kw)

        self.setupUi(self)
