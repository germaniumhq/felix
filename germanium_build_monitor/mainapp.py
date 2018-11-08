from typing import Dict, Any

from mopyx import render_call, action
import sys
import subprocess

from PySide2.QtWidgets import QMenu

from germanium_build_monitor.ui.MainDialog import MainDialog
from germanium_build_monitor.ui.core import \
    create_qt_application, \
    create_qt_tray_icon, \
    show_notification, \
    ui_thread_call

from germanium_build_monitor.model.RootModel import root_model
from germanium_build_monitor.model.BuildStatus import BuildStatus
from germanium_build_monitor.model.SystrayItem import SystrayItem
from germanium_build_monitor.model.JenkinsServer import JenkinsServer, jenkins_server

from germanium_build_monitor.model.jenkins.remote.read_build_jobs import read_build_job_branches
from germanium_build_monitor.model.jenkins.operations import compare_branches

import germanium_build_monitor.resources.icons as icons
import threading
import time


monitoring_threads: Dict[JenkinsServer, Any] = dict()


def exit_application():
    monitoring_threads.clear()
    sys.exit(0)


class JobMonitorThread(threading.Thread):
    def __init__(self,
                 server: JenkinsServer):
        super().__init__()
        self.server = server

    def run(self) -> None:
        print(f"Server {self.server.name} is being monitored")
        while self.server in monitoring_threads:
            for job in self.server.monitored_jobs.copy():
                print(f"scanning: {job.name}")
                result = jenkins_server(self.server).get_job_info(job.full_name, depth="2")
                updated_branches = read_build_job_branches(job.name, result)

                # run on UI
                @ui_thread_call
                @action
                def update_results() -> None:
                    if job.branches is None:
                        job.branches = updated_branches
                        return

                    notifications = compare_branches(job.branches, updated_branches)
                    job.branches = updated_branches

                    for notification in notifications:
                        if notification.branch.status == BuildStatus.SUCCESS:
                            icon = icons.get_icon("success128.png")
                        else:
                            icon = icons.get_icon("failed128.png")

                        show_notification(
                            notification.branch.project_name,
                            notification.branch.branch_name,
                            icon
                        )

                        systray_item = SystrayItem(
                            notification.branch.status,
                            f"{notification.branch.project_name} {notification.branch.decoded_branch_name}",
                            lambda: subprocess.Popen(["xdg-open", notification.build.url])
                        )
                        root_model.systray_items.append(systray_item)

            time.sleep(10)
        print(f"Stopped monitoring {self.server.name}")


menu = None


def main() -> None:
    app = create_qt_application()

    tray_icon = create_qt_tray_icon()
    tray_icon.setIcon(icons.get_icon("favicon.ico"))
    tray_icon.show()

    menu = QMenu()

    @render_call
    def render_context_menu():
        print("rendering new context menu")

        menu.clear()
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
                systray_item.action()

        menu.addSeparator()
        menu.addAction("Exit")\
            .triggered.connect(exit_application)

        print("all is good")

    tray_icon.setContextMenu(menu)

    @render_call
    def start_monitoring_threads():
        for server in root_model.servers:
            @render_call
            def start_monitoring_jobs_for_server():
                if server in monitoring_threads:
                    return

                thread = JobMonitorThread(server)
                monitoring_threads[server] = thread
                thread.start()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
