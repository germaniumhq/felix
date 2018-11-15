from typing import List, Optional, Dict, Any
from mopyx import model

from .JenkinsJobBranch import JenkinsJobBranch


@model
class JenkinsMonitoredJob:
    def __init__(self,
                 name: str,
                 full_name: str):
        self.name: str = name
        self.full_name: str = full_name
        self.branches: Optional[List[JenkinsJobBranch]] = None

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "full_name": self.full_name,
        }

    @staticmethod
    def from_dict(d) -> 'JenkinsMonitoredJob':
        return JenkinsMonitoredJob(
            name=d["name"],
            full_name=d["full_name"]
        )
