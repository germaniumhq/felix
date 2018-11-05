from mopyx import render, render_call
from PySide2.QtWidgets import QWidget

from PySide2.QtWidgets import QTreeWidgetItem
from PySide2.QtCore import Qt

from germanium_build_monitor.ui.Ui_SelectJobsFrame import Ui_Form

from germanium_build_monitor.model.JenkinsServer import JenkinsServer
from germanium_build_monitor.model.JenkinsFolder import JenkinsFolder


class SelectJobsFrame(QWidget, Ui_Form):
    def __init__(self, server: JenkinsServer) -> None:
        super().__init__()

        self.model = server

        self.setupUi(self)
        self.update_from_model()

    @render
    def update_from_model(self):
        self.update_root_level(self.tree_widget, self.model)

    @render
    def update_root_level(self,
                          parent_node,
                          server: JenkinsServer):
        for sub_folder in server.folders:
            child_node = QTreeWidgetItem()
            child_node.setFlags(child_node.flags() | Qt.ItemIsUserCheckable)
            child_node.setCheckState(0, Qt.Checked)

            parent_node.addTopLevelItem(child_node)

            def update_node_data():
                child_node.setText(0, sub_folder.name)

            render_call(update_node_data)
            self.update_folder_level(child_node, sub_folder)

        for job in server.jobs:
            child_node = QTreeWidgetItem()
            child_node.setFlags(child_node.flags() | Qt.ItemIsUserCheckable)
            child_node.setCheckState(0, Qt.Checked)

            parent_node.addTopLevelItem(child_node)

            def update_node_data():
                child_node.setText(0, job.name)

            render_call(update_node_data)

    @render
    def update_folder_level(self,
                            parent_node,
                            folder: JenkinsFolder):
        for sub_folder in folder.folders:
            child_node = QTreeWidgetItem()
            child_node.setFlags(child_node.flags() | Qt.ItemIsUserCheckable)
            child_node.setCheckState(0, Qt.Checked)

            parent_node.addChild(child_node)

            def update_node_data():
                child_node.setText(0, sub_folder.name)

            render_call(update_node_data)

        for job in folder.jobs:
            child_node = QTreeWidgetItem()
            child_node.setFlags(child_node.flags() | Qt.ItemIsUserCheckable)
            child_node.setCheckState(0, Qt.Checked)

            parent_node.addChild(child_node)

            def update_node_data():
                child_node.setText(0, job.name)

            render_call(update_node_data)

