from typing import List

import unittest

from germanium_build_monitor.model.RootModel import RootModel
from germanium_build_monitor.model.JenkinsServer import JenkinsServer
from germanium_build_monitor.model.JenkinsJob import JenkinsJob
from germanium_build_monitor.model.Folder import Folder
from germanium_build_monitor.model.JenkinsJobBranch import JenkinsJobBranch
from germanium_build_monitor.model.SystrayItem import SystrayItem
from germanium_build_monitor.model.operations import \
    server_add, \
    folder_add, \
    job_add


class TestSerialization(unittest.TestCase):
    recorded_events = []
    expected_events = ["wut"]

    """
    Tests if the serialization works as expected.
    """
    def test_persisting_a_model(self):
        """
        Test persisting a root model with some projects
        in it. Listeners should _not_ be serialized.
        """
        root = RootModel()

        server1 = server_add(root,
                             name="localhost",
                             url="http://jenkins:30000/",
                             use_authentication=True,
                             user="admin",
                             password="admin")

        folder1 = folder_add(server1,
                             name="folder1",
                             systray=True)

        folder2 = folder_add(server1,
                             name="folder2",
                             systray=False)

        job1 = job_add(server1,
                       name="Simple job 1",
                       url_part="/job/job1",
                       systray=True)

        job2 = job_add(server1,
                       name="Simple job 2",
                       url_part="/job/job2",
                       systray=False)

        folder1_job1 = job_add(folder1,
                               name="Simple job 1 in folder 1",
                               url_part="/job/folder1/job/job1",
                               systray=True)

        folder1_job2 = job_add(folder1,
                               name="Simple job 2 in folder 1",
                               url_part="/job/folder1/job/job2",
                               systray=False)

        folder1_job3 = job_add(folder1,
                               name="Simple job 3 in folder 1",
                               url_part="/job/folder1/job/job3",
                               systray=True)

        folder2_job1 = job_add(folder2,
                               name="Simple job 1 in folder 2",
                               url_part="/job/folder2/job/job1",
                               systray=True)

        folder2_job2 = job_add(folder1,
                               name="Simple job 2 in folder 2",
                               url_part="/job/folder2/job/job2",
                               systray=False)

        folder2_job3 = job_add(folder1,
                               name="Simple job 3 in folder 2",
                               url_part="/job/folder2/job/job3",
                               systray=True)

        self.assertEqual(6, len(root.systray_items),
                         "Systray item count is different.")


if __name__ == '__main__':
    unittest.main()
