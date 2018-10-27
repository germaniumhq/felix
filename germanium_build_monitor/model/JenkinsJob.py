from germanium_build_monitor.model.Folder import Folder


class JenkinsJob(Folder):
    """
    A Jenkins monitored job.
    """
    def __init__(self,
                 name: str,
                 url_part: str,
                 systray_avaialable: bool) -> None:
        super(Folder, self).__init__(name)

        self.url_part = url_part
        self.systray_avaialable = systray_avaialable
        self.branches = []

