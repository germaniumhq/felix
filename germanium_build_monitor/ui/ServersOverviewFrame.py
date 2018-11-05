from PySide2.QtWidgets import QWidget

from germanium_build_monitor.ui.generated.Ui_ServersOverviewFrame import Ui_Form


class ServersOverviewFrame(QWidget, Ui_Form):
    def __init__(self) -> None:
        super().__init__()

        self.setupUi(self)
