from typing import List

from .JenkinsServer import JenkinsServer
from .Observable import Observable
from .SystrayItem import SystrayItem


class RootModel(Observable):
    """
    Root model of the application.
    """

    def __init__(self) -> None:
        super().__init__()

        self.servers: List[JenkinsServer] = []
        self.systray_items: List[SystrayItem] = []

