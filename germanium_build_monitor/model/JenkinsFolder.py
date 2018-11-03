from typing import List
from mopyx import model

from .JenkinsJob import JenkinsJob


@model
class JenkinsFolder:
    def __init__(self, name: str):
        super().__init__()

        self.name = name

        self.folders: List['JenkinsFolder'] = []
        self.jobs: List[JenkinsJob] = []

    def as_dict(self):
        return {
            "name": self.name,
            "type": "JenkinsFolder",
            "folders": [x.as_dict() for x in self.folders],
            "jobs": [x.as_dict() for x in self.jobs],
        }
