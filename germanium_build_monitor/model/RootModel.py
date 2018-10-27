from typing import List

from .JenkinsServer import JenkinsServer


class RootModel():
    """
    Root model of the application.
    """

    def __init__(self) -> None:
        self.servers: List[JenkinsServer] = []

