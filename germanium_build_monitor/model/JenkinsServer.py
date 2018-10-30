from typing import Optional

from .JenkinsJob import JenkinsJob
from .Folder import Folder


class JenkinsServer(Folder):
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
        super().__init__(
            root=root,
            parent=None,
            name=name,
            systray=False)

        self.url = url
        self.use_authentication = use_authentication
        self.user = user
        self.password = password
        pass

