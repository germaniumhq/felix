from mopyx import model
from enum import Enum


class Selection(Enum):
    UNSELECTED = 'unselected'
    SELECTED = 'selected'
    PARTIAL = 'partial'


@model
class JenkinsJob:
    def __init__(self,
                 name: str,
                 full_name: str,
                 url: str):
        super().__init__()
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

