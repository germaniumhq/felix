from typing import Any, List

from germanium_build_monitor.model.JenkinsJobBranch import JenkinsJobBranch
from germanium_build_monitor.model.JenkinsJobBranchBuild import JenkinsJobBranchBuild
from germanium_build_monitor.model.BuildStatus import BuildStatus


def read_build_job_branches(project_name: str,
                            result: Any) -> List[JenkinsJobBranch]:

    if result["_class"] == "org.jenkinsci.plugins.workflow.job.WorkflowJob":
        return [read_single_job_branch(project_name, result)]
    elif result["_class"] == "org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject":
        branches = []

        for job in result["jobs"]:
            branch = read_single_job_branch(project_name, job)
            branches.append(branch)

        return branches
    else:
        raise Exception("Unsupported job type: " + str(result))


def read_single_job_branch(project_name: str, job: Any) -> JenkinsJobBranch:
    branch_name = job["name"]
    status = status_from_color(job["color"])

    branch = JenkinsJobBranch(
        project_name=project_name,
        branch_name=branch_name,
        status=status)

    for build in job["builds"]:
        if build["building"]:
            build_status = BuildStatus.RUNNING
        elif build["result"] == "FAILURE":
            build_status = BuildStatus.FAILURE
        else:
            build_status = BuildStatus.SUCCESS

        # FIXME: duration, and estimatedDuration also available

        build_timestamp = build["building"]
        build_url = build["url"]
        build_name = build["displayName"]

        build = JenkinsJobBranchBuild(name=build_name,
                                      status=build_status,
                                      url=build_url,
                                      timestamp=build_timestamp)
        branch.builds.append(build)

    return branch


def status_from_color(color: str) -> BuildStatus:
    status = BuildStatus.SUCCESS if color == "blue" else BuildStatus.FAILURE
    return status
