from typing import List

from mopyx import model
import urllib.parse

from .BuildStatus import BuildStatus
from .JenkinsJobBranchBuild import JenkinsJobBranchBuild


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
