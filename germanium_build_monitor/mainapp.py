import sys
from mopyx import render_call

from PySide2.QtWidgets import QMenu

from germanium_build_monitor.ui.MainDialog import MainDialog
from germanium_build_monitor.ui.core import create_qt_application, create_qt_tray_icon
from germanium_build_monitor.model.RootModel import model as root_model
from germanium_build_monitor.model.BuildStatus import BuildStatus

import germanium_build_monitor.resources.icons as icons


def exit_application():
    sys.exit(0)


def main() -> None:
    app = create_qt_application()

    tray_icon = create_qt_tray_icon()
    tray_icon.setIcon(icons.get_icon("favicon.ico"))
    tray_icon.show()

    global menu

    @render_call
    def render_context_menu():
        global menu

        if menu:
            menu.close()

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
