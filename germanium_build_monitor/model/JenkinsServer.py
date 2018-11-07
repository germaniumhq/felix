from typing import Optional

from mopyx import model

from .JenkinsFolder import JenkinsFolder


@model
class JenkinsServer(JenkinsFolder):
    def __init__(
            self,
            name: str = "",
            url: str = "http://localhost:8080/",
            use_authentication: bool = False,
            user: str = "",
            password: str = ""):

        super().__init__(
            parent=None,
            name=name)

        self.url = url
        self.use_authentication = use_authentication
        self.user = user
        self.password = password

    def as_dict(self):
        return {
            "name": self.name,
            "type": "JenkinsServer",

            "url": self.url,
            "use_authentication": self.use_authentication,
            "user": self.user,
            "password": self.password,

            "folders": [x.as_dict() for x in self.folders],
            "jobs": [x.as_dict() for x in self.jobs],
        }
