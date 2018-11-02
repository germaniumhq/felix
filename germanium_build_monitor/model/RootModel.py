from typing import List

from mopyx import model


@model
class RootModel:
    """
    Root model of the application.
    """

    def __init__(self) -> None:
        self.servers: List[JenkinsServer] = []
        self.systray_items: List[SystrayItem] = []

        self.tree_selection = None


model = RootModel()

from .JenkinsServer import JenkinsServer
from .SystrayItem import SystrayItem

model.servers.append(
    JenkinsServer(
        root=model,
        name='bmbzl',
        url='http://jenkins:30000',
        use_authentication=True,
        user="raptor",
        password="wut"
    ))

