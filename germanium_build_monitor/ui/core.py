from typing import Callable

import sys
import threading
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QMetaObject, QObject, Qt, QThread, Slot
from queue import Queue

app = None


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


def invoke_in_main_thread(func, *args):
    invoker.invoke(func, *args)


class GeThread(threading.Thread):
    def __init__(self,
                 target: Callable,
                 done: Callable) -> None:
        super().__init__()

        self.target = target
        self.done = done

    def run(self):
        self.target()
        invoke_in_main_thread(self.done)

