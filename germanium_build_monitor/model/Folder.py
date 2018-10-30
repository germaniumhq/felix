from typing import Optional, List

from .SystrayItem import SystrayItem
from .JenkinsJob import JenkinsJob


class Folder(SystrayItem):
    """
    A user defined folder.
    """
    def __init__(self,
                 root: 'RootModel',
                 parent: Optional['Folder'],
                 name: str,
                 systray: bool) -> None:
        super().__init__(systray=systray)

        self.name = name
        self.root: RootModel = root
        self.parent = parent

        self.folders: List['Folder'] = []
        self.jobs: List[JenkinsJob] = []

