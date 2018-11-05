from germanium_build_monitor.model.JenkinsServer import JenkinsServer

from germanium_build_monitor.ui.AddServerDialog import AddServerDialog
from germanium_build_monitor.ui.jobs_from_server.AddJobsFromServerDialog import AddJobsFromServerDialog
from germanium_build_monitor.ui.MainDialog import MainDialog


def open_create_jenkins_server_dialog():
    """ Open the add server dialog. """
    main_dialog = MainDialog.instance()

    AddServerDialog(
        JenkinsServer(
            name="",
            url="http://localhost:8080/",
            use_authentication=False,
            user="",
            password=""
        ),
        main_window=main_dialog,
        edit_mode=False,
    ).show()


def select_jobs_from_jenkins_server_dialog():
    main_dialog = MainDialog.instance()

    server = JenkinsServer(
        name="jenkins",
        url="http://jenkins:30001/",
        use_authentication=False,
        user="admin",
        password="admin"
    )

    AddJobsFromServerDialog(
        server,
        main_window=main_dialog,
        edit_mode=False,
    ).show()
