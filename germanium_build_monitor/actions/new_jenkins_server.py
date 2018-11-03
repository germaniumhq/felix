from germanium_build_monitor.model.RootModel import model
from germanium_build_monitor.model.JenkinsServer import JenkinsServer

from germanium_build_monitor.ui.AddServerDialog import AddServerDialog
from germanium_build_monitor.ui.MainWindow import MainWindow


def open_create_jenkins_server_dialog():
    """ Open the add server dialog. """
    main_window = MainWindow.instance()

    AddServerDialog(
        JenkinsServer(
            root=model,
            name="",
            url="http://localhost:8080/",
            use_authentication=False,
            user="",
            password=""
        ),
        main_window=main_window,
        edit_mode=True,
    ).show()


def edit_jenkins_server_dialog(server: JenkinsServer):
    main_window = MainWindow.instance()

    AddServerDialog(server, main_window).show()
