
from mopyx import model


@model
class JenkinsServer:
    def __init__(
            self,
            name: str = "",
            url: str = "http://localhost:8080/",
            use_authentication: bool = False,
            user: str = "",
            password: str = ""):

        self.name = name
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

        }
