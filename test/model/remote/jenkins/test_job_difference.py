from typing import List, Optional
import unittest

from germanium_build_monitor.model.remote.jenkins.read_build_jobs import read_build_job_branches
from .test_jenkins_build_loading import load_result

from germanium_build_monitor.model.JenkinsJobBranch import JenkinsJobBranch
from germanium_build_monitor.model.JenkinsJobBranchBuild import JenkinsJobBranchBuild
from germanium_build_monitor.model.BuildStatus import BuildStatus
from germanium_build_monitor.model.Notification import Notification


def compare_branches(initial_branches: List[JenkinsJobBranch],
                     updated_branches: List[JenkinsJobBranch]):
    notifications = []

    for branch in updated_branches:
        if not find_branch(initial_branches, branch):
            if branch.status == BuildStatus.SUCCESS or branch.status == BuildStatus.FAILED:
                notifications += Notification()

    for initial_branch in initial_branches:
        updated_branch = find_branch(updated_branches, initial_branch)

        if not updated_branch:
            continue

        if len(updated_branch.builds) != len(initial_branch.builds):
            last_build = get_last_finished_build(updated_branch)
            print(last_build._mopyx_target)
            if last_build.status == BuildStatus.SUCCESS or last_build.status == BuildStatus.FAILED:
                notifications += Notification()  # FIXME: state changes only?

    return notifications


def find_branch(branch_list: List[JenkinsJobBranch],
                searched_branch: JenkinsJobBranch) -> Optional[JenkinsJobBranch]:

    for branch in branch_list:
        if branch.branch_name == searched_branch.branch_name:
            return branch

    return None


def get_last_finished_build(branch: JenkinsJobBranch) -> JenkinsJobBranchBuild:
    return branch.builds[-1]


class TestJobDifferencesInBuild(unittest.TestCase):
    """
    Checks if the notifications can be updated.
    """

    def test_new_branch_failure(self):
        """
        Checks the detection.
        """
        initial_run = load_result("jd_build_initial.json")
        initial_branches = read_build_job_branches("jd", initial_run)

        branch_rerun = load_result("jd_build_a_feature_wut_rerun.json")
        rerun_branches = read_build_job_branches("jd", branch_rerun)

        notifications = compare_branches(initial_branches, rerun_branches)

if __name__ == '__main__':
    unittest.main()
