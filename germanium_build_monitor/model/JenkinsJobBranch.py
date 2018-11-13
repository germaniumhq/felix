from typing import List

from mopyx import model, computed
import urllib.parse

from .BuildStatus import BuildStatus
from .JenkinsJobBranchBuild import JenkinsJobBranchBuild

from .Settings import settings


@model
class JenkinsJobBranch:
    def __init__(self,
                 project_name: str,
                 branch_name: str,
                 status: BuildStatus):
        self.project_name = project_name
        self.branch_name = branch_name
        self.decoded_branch_name = urllib.parse.unquote(branch_name)
        self.status = status
        self.builds: List[JenkinsJobBranchBuild] = []

    @computed
    def last_builds(self) -> List[JenkinsJobBranchBuild]:
        result = list(self.builds)
        result.sort(key=lambda it: it.timestamp, reverse=True)

        result = result[0:settings.last_builds_count]

        return result
