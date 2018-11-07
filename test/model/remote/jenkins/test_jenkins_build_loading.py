from typing import Any

import unittest
import json
import os

from germanium_build_monitor.model.jenkins.remote.read_build_jobs import read_build_job_branches
from germanium_build_monitor.model.BuildStatus import BuildStatus


def load_result(json_file: str) -> Any:
    with open(os.path.join("test/model/remote/jenkins", json_file), "rt", encoding="utf-8") as f:
        return json.loads(f.read())


class TestJenkinsJobLoading(unittest.TestCase):
    """
    Tests if we can load the builds correctly
    """

    def test_jenkins_multibranch_jd_job_loading(self):
        """
        Try to fetch the builds from one of dem previously saved JSON files.
        """
        result = load_result("jd_build_initial.json")
        branches = read_build_job_branches("jd", result)

        self.assertTrue(branches)
        self.assertEqual(2, len(branches))

        self.assertEqual("feature/wut", branches[0].decoded_branch_name)
        self.assertEqual(BuildStatus.FAILURE, branches[0].status)
        self.assertEqual(1, len(branches[0].builds))

        self.assertEqual("master", branches[1].decoded_branch_name)
        self.assertEqual(BuildStatus.SUCCESS, branches[1].status)
        self.assertEqual(17, len(branches[1].builds))

    def test_jenkins_multibranch_jd_job_rerun(self):
        """
        Try to fetch the builds from one of dem previously saved JSON files.
        """
        result = load_result("jd_build_a_feature_wut_rerun.json")
        branches = read_build_job_branches("jd", result)

        self.assertTrue(branches)
        self.assertEqual(2, len(branches))

        self.assertEqual("feature/wut", branches[0].decoded_branch_name)
        self.assertEqual(BuildStatus.FAILURE, branches[0].status)
        self.assertEqual(2, len(branches[0].builds))

        self.assertEqual("master", branches[1].decoded_branch_name)
        self.assertEqual(BuildStatus.SUCCESS, branches[1].status)
        self.assertEqual(17, len(branches[1].builds))

    def test_basic_loading(self):
        """
        Try to fetch the builds from one of dem previously saved JSON files.
        """
        result = load_result("ww_build_initial.json")
        branches = read_build_job_branches("ww", result)

        self.assertTrue(branches)
        self.assertEqual(1, len(branches))

        self.assertEqual("ww", branches[0].decoded_branch_name)
        self.assertEqual(BuildStatus.SUCCESS, branches[0].status)
        self.assertEqual(3, len(branches[0].builds))

    def test_jenkins_multibranch_x_job_loading(self):
        """
        Try to fetch the builds from one of dem previously saved JSON files.
        """
        result = load_result("x_build_initial.json")
        branches = read_build_job_branches("x", result)

        self.assertTrue(branches)
        self.assertEqual(1, len(branches))

        self.assertEqual("master", branches[0].decoded_branch_name)
        self.assertEqual(BuildStatus.SUCCESS, branches[0].status)
        self.assertEqual(3, len(branches[0].builds))


if __name__ == '__main__':
    unittest.main()
