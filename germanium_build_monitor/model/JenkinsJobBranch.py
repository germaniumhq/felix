from germanium_build_monitor.model.ActionType import ActionType
from germanium_build_monitor.model.NotificationStrategy import NotificationStrategy

from .Observable import Observable


class JenkinsJobBranch(Observable):
    """
    A branch in Jenkins
    """
    def __init__(self,
                 expression: str,
                 action: ActionType,
                 notification: NotificationStrategy) -> None:
        super().__init__()

        self.expression = expression
        self.action = action
        self.notification = notification

