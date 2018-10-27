from typing import Optional


class JenkinsServer:
    """
    A Jenkins Server definition
    """
    def __init__(self,
                 name: str,
                 url: str,
                 use_authentication: bool,
                 user: Optional[str],
                 password: Optional[str]) -> None:
        self.name = name
        self.url = url
        self.use_authentication = use_authentication
        self.user = user
        self.password = password
        pass

