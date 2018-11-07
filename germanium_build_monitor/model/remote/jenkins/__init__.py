from typing import Any, List

from germanium_build_monitor.model.JenkinsJobBranch import JenkinsJobBranch
from germanium_build_monitor.model.JenkinsJobBranchBuild import JenkinsJobBranchBuild
from germanium_build_monitor.model.BuildStatus import BuildStatus


def read_job_builds(result: Any) -> List[JenkinsJobBranch]:
    branches = []

    for job in result["jobs"]:
        branch_name = job["name"]
        status = BuildStatus.SUCCESS if job["color"] == "blue" else BuildStatus.FAILURE

        branches.append(JenkinsJobBranch(branch_name=branch_name,
                                         status=status))

    return branches
