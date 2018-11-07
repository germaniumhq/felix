from typing import Optional

from mopyx import model
from enum import Enum

from .JenkinsFolder import JenkinsFolder


class Selection(Enum):
    UNSELECTED = 'unselected'
    SELECTED = 'selected'
    PARTIAL = 'partial'


@model
class JenkinsJob:
    def __init__(self,
                 parent: Optional[JenkinsFolder],
                 name: str,
                 full_name: str,
                 url: str):
        super().__init__()

        self.parent = parent

        self.name = name
        self.full_name = full_name
        self.url = url
        self.selected = Selection.SELECTED

    def as_dict(self):
        return {
            "type": "JenkinsJob",
            "full_name": self.full_name,
            "name": self.name,
            "url": self.url
        }

