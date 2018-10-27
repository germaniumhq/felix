from typing import Optional, List

from .JenkinsJob import JenkinsJob


class Folder:
    """
    A user defined folder.
    """
    name: str
    description: Optional[str]
    folders: List['Folder']
    jobs: List[JenkinsJob]

    def __init__(self,
                 name: str,
                 description: Optional[str]) -> None:
        self.name = name
        self.description = description
        self.folders = []
        self.jobs = []
