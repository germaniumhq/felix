from germanium_build_monitor.model.RootModel import model
from germanium_build_monitor.model.JenkinsServer import JenkinsServer

from germanium_build_monitor.ui.AddServerDialog import AddServerDialog
from germanium_build_monitor.ui.MainWindow import MainWindow

def open_create_jenkins_server_dialog():
    """ Open the add server dialog. """
    print("open dialog")
    AddServerDialog(
        JenkinsServer(
            root=model,
            name=u"a",
            url=u"http://localhost:8080/",
            use_authentication=False,
            user=u"",
            password=u""
        ),
        MainWindow.instance()).show()
