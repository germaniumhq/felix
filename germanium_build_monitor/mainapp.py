import sys
from mopyx import render_call

from PySide2.QtWidgets import QSystemTrayIcon, QMenu

from germanium_build_monitor.ui.MainDialog import MainDialog
from germanium_build_monitor.ui.core import create_qt_application
from germanium_build_monitor.model.RootModel import model as root_model
from germanium_build_monitor.model.BuildStatus import BuildStatus

import germanium_build_monitor.resources.icons as icons


def exit_application():
    sys.exit(0)


def main() -> None:
    app = create_qt_application()

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

    @render_call
    def render_context_menu():
        menu = QMenu()
        menu.addAction(icons.get_icon("favicon.ico"), "Main Window") \
            .triggered.connect(MainDialog.instance().show)

        if root_model.systray_items:
            menu.addSeparator()

            for systray_item in root_model.systray_items:
                if systray_item.status == BuildStatus.SUCCESS:
                    icon = icons.get_icon("success128.png")
                else:
                    icon = icons.get_icon("failed128.png")

                menu.addAction(icon, systray_item.text)\
                    .triggered.connect(systray_item.action)

        menu.addSeparator()
        menu.addAction("Exit")\
            .triggered.connect(exit_application)

        tray_icon.setContextMenu(menu)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
