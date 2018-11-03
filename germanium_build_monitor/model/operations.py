from mopyx import action

from .RootModel import RootModel
from .JenkinsServer import JenkinsServer
from .Folder import Folder
from .JenkinsJob import JenkinsJob


@action
def server_add(root: RootModel,
               server: JenkinsServer) -> None:
    root.servers.append(server)


@action
def folder_add(parent: Folder,
               name: str,
               systray: bool) -> Folder:
    """
    Create a folder.
    """

    folder = Folder(
        root=parent.root,
        parent=parent,
        name=name,
        systray=systray)

    parent.folders.append(folder)

    if folder.systray:
        parent.root.systray_items.append(folder)

    return folder


@action
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

    if job.systray:
        parent.root.systray_items.append(job)

    return job

