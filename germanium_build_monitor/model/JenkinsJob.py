from mopyx import model


@model
class JenkinsJob:
    def __init__(self,
                 name: str,
                 full_name: str,
                 url: str):
        super().__init__()
        self.name = name
        self.full_name = full_name
        self.url = url

    def as_dict(self):
        return {
            "type": "JenkinsJob",
            "full_name": self.full_name,
            "name": self.name,
            "url": self.url
        }

