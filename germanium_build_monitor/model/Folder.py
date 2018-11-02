from typing import Optional, List

from mopyx import model


@model
class Folder:
    """
    A user defined folder.
    """
    def __init__(self,
                 root: 'RootModel',
                 parent: Optional['Folder'],
                 name: str,
                 systray: bool) -> None:
        self.systray = systray

        self.name = name
        self.root: 'RootModel' = root
        self.parent = parent

        self.folders: List['Folder'] = []
        self.jobs: List[JenkinsJob] = []


from .JenkinsJob import JenkinsJob
from .RootModel import RootModel