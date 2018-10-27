from enum import Enum


class ActionType(Enum):
    """
    What actions can be performed on a branch.
    """
    MONITOR = "monitor"
    IGNORE = "ignore"

