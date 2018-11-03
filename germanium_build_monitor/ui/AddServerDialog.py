from mopyx import render_call
import jenkins
import traceback

from PySide2.QtWidgets import QDialog, QMessageBox, QWidget

from germanium_build_monitor.ui.Ui_AddServerDialog import Ui_Dialog

from germanium_build_monitor.model.JenkinsServer import JenkinsServer


def not_empty(s: str) -> bool:
    return bool(s and s.strip())


class AddServerDialog(QDialog, Ui_Dialog):
    def __init__(self,
                 model: JenkinsServer,
                 main_window: QWidget,
                 edit_mode: bool = False,
                 ) -> None:
        super().__init__(main_window)

        self.model = model
        self.edit_mode = edit_mode  # are we adding, or editing?

        self.setupUi(self)

        self.update_labels()

        self.wire_signals()
        self.update_from_model()

    def update_labels(self):
        if not self.edit_mode:
            return

        self.add_button.hide()
        self.setWindowTitle("Edit server...")

    def wire_signals(self):
        self.name_edit.textEdited.connect(self.update_name)
        self.url_edit.textEdited.connect(self.update_url)
        self.auth_check_box.clicked.connect(self.update_auth_status)
        self.user_edit.textEdited.connect(self.update_user)
        self.password_edit.textEdited.connect(self.update_password)

        self.add_button.clicked.connect(self.add_server)
        self.test_server_button.clicked.connect(self.test_server)
        self.close_button.clicked.connect(self.hide)

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
        def update_auth_status():
            self.user_edit.setEnabled(self.model.use_authentication)
            self.password_edit.setEnabled(self.model.use_authentication)
            self.user_label.setEnabled(self.model.use_authentication)
            self.password_label.setEnabled(self.model.use_authentication)

        render_call(update_auth_status)

        render_call(lambda: self.add_button.setEnabled(
            not_empty(self.model.name) and not_empty(self.model.url)))

        render_call(lambda: self.test_server_button.setEnabled(not_empty(self.model.url)))

        # no need to be reactive from these ones
        self.name_edit.setText(self.model.name)
        self.url_edit.setText(self.model.url)
        self.auth_check_box.setChecked(self.model.use_authentication)
        self.user_edit.setText(self.model.user)
        self.password_edit.setText(self.model.password)

    def add_server(self):
        self.close()

    def test_server(self):
        try:
            if self.model.use_authentication:
                server = jenkins.Jenkins(self.model.url,
                                         username=self.model.user,
                                         password=self.model.password)
            else:
                server = jenkins.Jenkins(self.model.url)

            server.get_whoami()
            version = server.get_version()

            QMessageBox.information(self,
                                    "Success",
                                    f"User {self.model.user} connected. Jenkins version {version}.")
        except Exception as e:
            error_message = QMessageBox()

            error_message.setWindowTitle(self.tr("Server Unavailable"))
            error_message.setText(self.tr("Error: ") + str(e))
            error_message.setDetailedText(traceback.format_exc())
            error_message.setIcon(QMessageBox.Critical)

            error_message.exec_()
