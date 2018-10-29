from .SystrayItem import SystrayItem


class JenkinsJob(SystrayItem):
    """
    A Jenkins monitored job.
    """
    def __init__(self,
                 parent: 'Folder',
                 name: str,
                 url_part: str,
                 systray: bool) -> None:
        super().__init__(
            systray=systray
        )

        self.name = name
        self.parent = parent
        self.url_part = url_part
        self.branches = []


from germanium_build_monitor.model.Folder import Folder
