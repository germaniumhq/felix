from enum import Enum


class NotificationStrategy(Enum):
    NEVER = "never"
    STATE_CHANGE = "state_change"
    ALWAYS = "always"
