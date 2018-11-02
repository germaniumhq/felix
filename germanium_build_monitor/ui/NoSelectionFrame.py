from PySide2.QtWidgets import QWidget

from germanium_build_monitor.ui.Ui_NoSelectionFrame import Ui_Form


class NoSelectionFrame(QWidget, Ui_Form):
    def __init__(self) -> None:
        super().__init__()

        self.setupUi(self)
