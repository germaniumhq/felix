import sys
import os

from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QMenu, QAction, QMessageBox, QSystemTrayIcon, QMenu

from germanium_build_monitor.ui.MainWindow import MainWindow
import germanium_build_monitor.resources.icons as icons


def exit_application():
    sys.exit(0)


def main() -> None:
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    def show_main_application():
        main_window.show()

    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(icons.get_icon("favicon.ico"))
    tray_icon.show()
    tray_icon.showMessage("WEBUI",
                          "bugfix/12.2/WEBUI-123-fix-the-bug-with-the-other-bug",
                          icons.get_icon('fail24.png'),
                          4000)

    tray_icon.setIcon(icons.get_icon("favicon.ico"))

    def show_custom_message(message: str):
        def show_msg():
            tray_icon.showMessage("WEBUI",
                                  message,
                                  icons.get_icon('success128.png'),
                                  4000)

        return show_msg

    menu = QMenu()
    menu.addAction(icons.get_icon("favicon.ico"), "Main Window") \
        .triggered.connect(show_main_application)

    menu.addSeparator()

    menu.addAction(icons.get_icon("failed128.png"),
                   "GermaniumSB")\
        .triggered.connect(show_custom_message("build failed"))
    menu.addAction(icons.get_icon("success128.png"),
                   "Wutinston")\
        .triggered.connect(show_custom_message("build failed"))

    menu.addSeparator()
    menu.addAction("Exit")\
        .triggered.connect(exit_application)

    tray_icon.setContextMenu(menu)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
