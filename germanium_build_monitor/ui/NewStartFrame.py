from PySide2.QtWidgets import QWidget

from germanium_build_monitor.ui.Ui_NewStartFrame import Ui_Form
from germanium_build_monitor.resources import icons

from germanium_build_monitor.actions.new_jenkins_server import open_create_jenkins_server_dialog
from germanium_build_monitor.actions.new_jenkins_server import select_jobs_from_jenkins_server_dialog


class NewStartFrame(QWidget, Ui_Form):
    def __init__(self) -> None:
        super(NewStartFrame, self).__init__()
        self.setupUi(self)

        self.add_server_button.setIcon(icons.get_icon("server24.png"))
        self.add_server_button.clicked.connect(select_jobs_from_jenkins_server_dialog)
