from typing import List, Optional, Dict, Any, Set
from mopyx import model


@model
class JenkinsMonitoredJob:
    def __init__(self,
                 name: str,
                 full_name: Optional[str] = None,
                 ignored_branches: Optional[Set[str]] = None):
        self.name: str = name
        self.full_name: str = full_name if full_name else name
        self.branches: Optional[List[JenkinsJobBranch]] = None
        self.ignored_branches: Set[str] = ignored_branches if ignored_branches else set()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "full_name": self.full_name,
            "ignored_branches": self.ignored_branches,
        }

    @staticmethod
    def from_dict(d) -> 'JenkinsMonitoredJob':
        return JenkinsMonitoredJob(
            name=d["name"],
            full_name=d["full_name"],
            ignored_branches=d.get("ignored_branches", set())
        )


from .JenkinsJobBranch import JenkinsJobBranch
