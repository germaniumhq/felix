from mopyx import render

from PySide2.QtWidgets import QDialog

from germanium_build_monitor.ui.Ui_AddServerDialog import Ui_Dialog
from germanium_build_monitor.model.JenkinsServer import JenkinsServer


class AddServerDialog(QDialog, Ui_Dialog):
    def __init__(self,
                 model: JenkinsServer,
                 *args,
                 **kw) -> None:
        super().__init__(*args, **kw)

        self.model = model

        self.setupUi(self)

        self.wire_signals()
        self.update_from_model()

    def wire_signals(self):
        self.name_edit.textEdited.connect(self.update_name)
        self.url_edit.textEdited.connect(self.update_url)
        self.auth_check_box.clicked.connect(self.update_auth_status)
        self.user_edit.textEdited.connect(self.update_user)
        self.password_edit.textEdited.connect(self.update_password)

    def update_name(self):
        self.model.name = self.name_edit.text()

    def update_url(self):
        self.model.url = self.url_edit.text()

    def update_auth_status(self):
        self.model.use_authentication = self.auth_check_box.isChecked()

    def update_user(self):
        self.model.user = self.user_edit.text()

    def update_password(self):
        self.model.password = self.password_edit.text()

    def update_from_model(self):
        @render
        def update_auth_status():
            self.user_edit.setEnabled(self.model.use_authentication)
            self.password_edit.setEnabled(self.model.use_authentication)

        update_auth_status()
        
        self.name_edit.setText(self.model.name)
        self.url_edit.setText(self.model.url)
        self.auth_check_box.setChecked(self.model.use_authentication)
        self.user_edit.setText(self.model.user)
        self.password_edit.setText(self.model.password)
