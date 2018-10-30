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

        expected_events: List = []
        root.on_event("server-new", self.register_new_server)
        root.on_event("server-update", self.register_update_server)
        root.on_event("server-delete", self.register_delete_server)
        root.on_event("systray-item-new", self.register_new_systray_item)
        root.on_event("systray-item-update", self.register_update_systray_item)
        root.on_event("systray-item-delete", self.register_delete_systray_item)

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

        self.assertEqual(self.expected_events,
                         self.recorded_events)

    def register_new_server(self, server: JenkinsServer) -> None:
        self.recorded_events.append("server-new")

        server.on_event("folder-new", self.register_new_folder)
        server.on_event("folder-update", self.register_update_folder)
        server.on_event("folder-delete", self.register_delete_folder)
        server.on_event("job-new", self.register_new_job)
        server.on_event("job-update", self.register_update_folder)
        server.on_event("job-delete", self.register_delete_job)

    def register_update_server(self, server: JenkinsServer) -> None:
        self.recorded_events.append("server-update")

    def register_delete_server(self, server: JenkinsServer) -> None:
        self.recorded_events.append("server-delete")

    def register_new_systray_item(self,
                                  item: SystrayItem,
                                  index: int) -> None:
        self.recorded_events.append(f"systray-item-new:{index}")

    def register_update_systray_item(self,
                                     item: SystrayItem) -> None:
        self.recorded_events.append("systray-item-update")

    def register_delete_systray_item(self,
                                     item: SystrayItem) -> None:
        self.recorded_events.append("systray-item-delete")

    def register_new_folder(self, folder: Folder) -> None:
        self.recorded_events.append("folder-new")

        folder.on_event("folder-new", self.register_new_folder)
        folder.on_event("folder-update", self.register_update_folder)
        folder.on_event("folder-delete", self.register_delete_folder)
        folder.on_event("job-new", self.register_new_job)
        folder.on_event("job-update", self.register_update_folder)
        folder.on_event("job-delete", self.register_delete_job)

    def register_update_folder(self, folder: Folder) -> None:
        self.recorded_events.append("folder-update")

    def register_delete_folder(self, folder: Folder) -> None:
        self.recorded_events.append("folder-delete")

    def register_new_job(self, folder: JenkinsJob) -> None:
        self.recorded_events.append("job-new")

        folder.on_event("branch-new", self.register_new_branch)
        folder.on_event("branch-delete", self.register_delete_branch)
        folder.on_event("branch-update", self.register_update_branch)
        folder.on_event("branch-move-up", self.register_move_up_branch)
        folder.on_event("branch-move-down", self.register_move_down_branch)

    def register_update_job(self, job: JenkinsJob) -> None:
        self.recorded_events.append("job-update")

    def register_delete_job(self, job: JenkinsJob) -> None:
        self.recorded_events.append("job-delete")

    def register_new_branch(self,
                            branch: JenkinsJobBranch) -> None:
        self.recorded_events.append("branch-new")

    def register_update_branch(self,
                               branch: JenkinsJobBranch) -> None:
        self.recorded_events.append("branch-update")

    def register_delete_branch(self,
                               branch: JenkinsJobBranch) -> None:
        self.recorded_events.append("branch-delete")

    def register_move_up_branch(self,
                                branch: JenkinsJobBranch,
                                old_index: int,
                                new_index: int) -> None:
        self.recorded_events.append(f"branch-move-up:{old_index}-{new_index}")

    def register_move_down_branch(self,
                                  branch: JenkinsJobBranch,
                                  old_index: int,
                                  new_index: int) -> None:
        self.recorded_events.append(f"branch-move-down:{old_index}-{new_index}")

if __name__ == '__main__':
    unittest.main()
