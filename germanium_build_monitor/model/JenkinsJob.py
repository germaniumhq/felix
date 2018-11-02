from mopyx import model


@model
class JenkinsJob:
    """
    A Jenkins monitored job.
    """
    def __init__(self,
                 parent: 'Folder',
                 name: str,
                 url_part: str,
                 systray: bool) -> None:
        self.systray = systray
        self.name = name
        self.parent = parent
        self.url_part = url_part
        self.branches = []


from .Folder import Folder
