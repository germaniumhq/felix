import sys

from PySide2.QtWidgets import QApplication, QSystemTrayIcon, QMenu

from germanium_build_monitor.ui.MainDialog import MainDialog
import germanium_build_monitor.resources.icons as icons


def exit_application():
    sys.exit(0)


def main() -> None:
    app = QApplication(sys.argv)

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
                                  icons.get_icon('fail24.png'),
                                  4000)

        return show_msg

    menu = QMenu()
    menu.addAction(icons.get_icon("favicon.ico"), "Main Window") \
        .triggered.connect(MainDialog.instance().show)

    menu.addSeparator()

    menu.addAction(icons.get_icon("failed128.png"),
                   "GermaniumSB")\
        .triggered.connect(show_custom_message("build failed"))
    menu.addAction(icons.get_icon("success128.png"),
                   "\u2610\u2611\u2612\u2611 Wutinston feature/PMIA-1141-add-new-bmbzling-feature")\
        .triggered.connect(show_custom_message("build failed"))

    menu.addSeparator()
    menu.addAction("Exit")\
        .triggered.connect(exit_application)

    tray_icon.setContextMenu(menu)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
