from typing import List

from mopyx import model
import urllib.parse

from .BuildStatus import BuildStatus
from .JenkinsJobBranchBuild import JenkinsJobBranchBuild


@model
class JenkinsJobBranch:
    def __init__(self,
                 branch_name: str,
                 status: BuildStatus):
        self.branch_name = branch_name
        self.decoded_branch_name = urllib.parse.unquote(branch_name)
        self.status = status
        self.known_builds: List[JenkinsJobBranchBuild] = []

