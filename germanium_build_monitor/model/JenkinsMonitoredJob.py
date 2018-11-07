from typing import List, Optional
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

