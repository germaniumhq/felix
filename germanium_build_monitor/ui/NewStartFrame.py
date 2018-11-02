from PySide2.QtWidgets import QWidget

from germanium_build_monitor.ui.Ui_NewStartFrame import Ui_Form
from germanium_build_monitor.resources import icons


class NewStartFrame(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(NewStartFrame, self).__init__()
        self.setupUi(self)

        self.add_server_button.setIcon(icons.get_icon("server24.png"))

        self.destroyed.connect(lambda: self.cleanup())

    def cleanup(self) -> None:
        print("cleanup")