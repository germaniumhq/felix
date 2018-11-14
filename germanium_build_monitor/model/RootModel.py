from typing import List, cast, Dict, Any

from mopyx import model

from .JenkinsServer import JenkinsServer
from .Systray import Systray


@model
class RootModel:
    """
    Root model of the application.
    """

    def __init__(self) -> None:
        super().__init__()

        self.servers: List[JenkinsServer] = []
        self.systray: Systray = Systray()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "servers": [server.as_dict() for server in self.servers]
        }

    @staticmethod
    def from_dict(d) -> 'RootModel':
        result = RootModel()

        result.servers = [JenkinsServer.from_dict(s) for s in d['servers']]

        return result


root_model = cast(RootModel, RootModel())

