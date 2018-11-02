from typing import Optional, List

from mopyx import model

from .RootModel import RootModel


@model
class JenkinsServer:
    """
    A Jenkins Server definition
    """
    def __init__(self,
                 root: 'RootModel',
                 name: str,
                 url: str,
                 use_authentication: bool,
                 user: Optional[str],
                 password: Optional[str]) -> None:
        self.url = url
        self.root = root,
        self.parent = None,

        self.folders: List['Folder'] = []
        self.jobs: List[JenkinsJob] = []

        self.name = name,
        self.systray = False
        self.use_authentication = use_authentication
        self.user = user
        self.password = password


from .JenkinsJob import JenkinsJob
from .Folder import Folder
