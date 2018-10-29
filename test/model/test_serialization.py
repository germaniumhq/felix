from typing import List

import unittest

from germanium_build_monitor.model.RootModel import RootModel
from germanium_build_monitor.model.JenkinsServer import JenkinsServer
from germanium_build_monitor.model.JenkinsJob import JenkinsJob
from germanium_build_monitor.model.Folder import Folder
from germanium_build_monitor.model.JenkinsJobBranch import JenkinsJobBranch
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

        expected_events: List = []
        root.on_event("server-new", self.register_new_server)

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
                               systray=True)

        folder2_job1 = job_add(folder2,
                               name="Simple job 1 in folder 2",
                               url_part="/job/folder2/job/job1",
                               systray=True)

        folder2_job2 = job_add(folder1,
                               name="Simple job 2 in folder 2",
                               url_part="/job/folder2/job/job2",
                               systray=True)

        self.assertEqual(self.expected_events,
                         self.recorded_events)

    def register_new_server(self, server: JenkinsServer) -> None:
        self.recorded_events.append("server-new")
        server.on_event("folder-new", self.register_new_folder)
        server.on_event("job-new", self.register_new_job)

    def register_new_folder(self, folder: Folder) -> None:
        self.recorded_events.append("folder-new")
        folder.on_event("folder-new", self.register_new_folder)
        folder.on_event("job-new", self.register_new_job)

    def register_new_job(self, folder: JenkinsJob) -> None:
        self.recorded_events.append("job-new")
        folder.on_event("branch-new", self.register_new_branch)

    def register_new_branch(self, branch: JenkinsJobBranch) -> None:
        self.recorded_events.append("branch-new")


if __name__ == '__main__':
    unittest.main()
