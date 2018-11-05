from typing import List

from mopyx import model

from .JenkinsServer import JenkinsServer
from .SystrayItem import SystrayItem


@model
class RootModel:
    """
    Root model of the application.
    """

    def __init__(self) -> None:
        super().__init__()

        self.servers: List[JenkinsServer] = []
        self.systray_items: List[SystrayItem] = []

        self.tree_selection = None


model = RootModel()  # type: ignore

