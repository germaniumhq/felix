from typing import Callable, TypeVar

import functools
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QMetaObject, QObject, Qt, Slot
from queue import Queue

app = None
T = TypeVar('T')


def create_qt_application() -> QApplication:
    global app

    if not app:
        app = QApplication(sys.argv)

    return app


class Invoker(QObject):
    def __init__(self):
        super(Invoker, self).__init__()
        self.queue = Queue()

    def invoke(self, func, *args):
        self.queue.put(lambda: func(*args))
        QMetaObject.invokeMethod(self, "handler", Qt.QueuedConnection)

    @Slot()
    def handler(self):
        f = self.queue.get()
        f()


invoker = Invoker()


def ui_thread_call(f: Callable[..., T]) -> Callable[..., T]:
    """
    Will call the given function on the PySide UI Thread.
    """
    @functools.wraps(f)
    def wrapper(*args, **kw) -> T:
        return invoker.invoke(f, *args, **kw)

    return wrapper()
