from typing import Callable, Any


class QEvent:
    def connect(self, callback: Callable[..., Any]) -> None:
        pass


class QTimer:
    def __init__(self, window) -> None:
        self.timeout = QEvent()

    def start(self, repeat_millis: int) -> None:
        pass

    def stop(self) -> None:
        pass

