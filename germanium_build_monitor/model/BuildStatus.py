import enum


class BuildStatus(enum.Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    RUNNING = "running"
    NEVER = "never"
