from germanium_build_monitor.model.JenkinsServer import JenkinsServer


def open_create_jenkins_server_dialog():
    """ Open the add server dialog. """
    main_dialog = MainDialog.instance()

    AddServerDialog(
        JenkinsServer(
            name="jenkins",
            url="http://jenkins:8080/",
            use_authentication=False,
            user="",
            password=""
        ),
        main_window=main_dialog,
        edit_mode=False,
    ).show()


def select_jobs_from_jenkins_server_dialog(server: JenkinsServer):
    main_dialog = MainDialog.instance()

    AddJobsFromServerDialog(
        server,
        main_window=main_dialog,
        edit_mode=False,
    ).show()


from germanium_build_monitor.ui.jenkins_add.AddServerDialog import AddServerDialog
from germanium_build_monitor.ui.jobs_from_server.AddJobsFromServerDialog import AddJobsFromServerDialog
from germanium_build_monitor.ui.MainDialog import MainDialog

