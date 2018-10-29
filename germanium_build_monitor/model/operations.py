from typing import Optional

from .RootModel import RootModel
from .JenkinsServer import JenkinsServer
from .Folder import Folder
from .JenkinsJob import JenkinsJob


def server_add(root: RootModel,
               name: str,
               url: str,
               use_authentication: bool,
               user: Optional[str],
               password: Optional[str]) -> JenkinsServer:
    """
    Create a new server into the root model.
    """
    server = JenkinsServer(
        name=name,
        url=url,
        use_authentication=use_authentication,
        user=user,
        password=password)

    root.servers.append(server)
    root.notify_observers("server-new", server)

    return server


def folder_add(parent: Folder,
               name: str,
               systray: bool) -> Folder:
    """
    Create a folder.
    """

    folder = Folder(
        parent=parent,
        name=name,
        systray=systray)

    parent.folders.append(folder)
    parent.notify_observers("folder-new", folder)

    return folder


def job_add(parent: Folder,
            name: str,
            url_part: str,
            systray: bool) -> JenkinsJob:
    """
    Create a new job.
    """
    job = JenkinsJob(
        parent=parent,
        name=name,
        url_part=url_part,
        systray=systray)

    parent.jobs.append(job)
    parent.notify_observers("job-new", job)

    return job

