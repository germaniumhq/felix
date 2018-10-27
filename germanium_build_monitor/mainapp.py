import sys
import os

from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QMenu, QAction, QMessageBox, QSystemTrayIcon

from germanium_build_monitor.ui.MainWindow import Ui_MainWindow
import germanium_build_monitor.resources.icons as icons


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setWindowIcon(icons.get_icon("favicon.ico"))

        self.setupUi(self)


def main() -> None:
    app = QApplication(sys.argv)

    QSystemTrayIcon()

    mainWin = MainWindow()
    mainWin.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
