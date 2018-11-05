from typing import Any
from mopyx import render, render_call, action
from PySide2.QtWidgets import QWidget

from PySide2.QtWidgets import QTreeWidgetItem
from PySide2.QtCore import Qt

from germanium_build_monitor.ui.generated.Ui_SelectJobsFrame import Ui_Form
from germanium_build_monitor.resources.icons import get_icon

from germanium_build_monitor.model.JenkinsServer import JenkinsServer
from germanium_build_monitor.model.JenkinsFolder import JenkinsFolder, Selection


def as_qt_selection(value: Selection):
    if value == Selection.UNSELECTED:
        return Qt.CheckState.Unchecked
    elif value == Selection.SELECTED:
        return Qt.CheckState.Checked
    elif value == Selection.PARTIAL:
        return Qt.CheckState.PartiallyChecked
    else:
        raise Exception(f"Unknown enum value for selection {value}")


def as_selection(value: 'Qt.CheckState'):
    if value == Qt.CheckState.Checked:
        return Selection.SELECTED
    elif value == Qt.CheckState.Unchecked:
        return Selection.UNSELECTED
    else:
        return Selection.PARTIAL


class SelectJobsFrame(QWidget, Ui_Form):
    def __init__(self, server: JenkinsServer) -> None:
        super().__init__()

        self.model = server

        self.setupUi(self)

        self.wire_signals()
        self.update_from_model()

    def wire_signals(self):
        def set_selection_down(node, selection):
            print(f"setting {node.name} as {selection}")
            node.selection = selection

            if isinstance(node, JenkinsFolder):
                for folder in node.folders:
                    set_selection_down(folder)

                for job in node.jobs:
                    job.selection = selection

        @action
        def item_changed(item, index):
            node = item.data(1, 0)
            selection = as_selection(item.checkState(index))
            set_selection_down(node, selection)

        self.tree_widget.itemChanged.connect(item_changed)

    @render
    def update_from_model(self):
        self.update_root_level()

    @render
    def update_root_level(self):
        for sub_folder in self.model.folders:
            child_node = create_node(sub_folder)

            self.tree_widget.addTopLevelItem(child_node)

            def update_node_data():
                child_node.setText(0, sub_folder.name)
                child_node.setIcon(0, get_icon("folder24.png"))
                child_node.setCheckState(0, as_qt_selection(sub_folder.selected))

            render_call(update_node_data, ignore_updates=True)
            self.update_folder_level(child_node, sub_folder)

        for job in self.model.jobs:
            child_node = create_node(job)

            self.tree_widget.addTopLevelItem(child_node)

            def update_node_data():
                child_node.setText(0, job.name)
                child_node.setIcon(0, get_icon("job24.png"))
                child_node.setCheckState(0, as_qt_selection(job.selected))

            render_call(update_node_data, ignore_updates=True)

    @render
    def update_folder_level(self,
                            parent_node,
                            folder: JenkinsFolder):
        for sub_folder in folder.folders:
            child_node = create_node(sub_folder)
            parent_node.addChild(child_node)

            def update_node_data():
                child_node.setText(0, sub_folder.name)
                child_node.setIcon(0, get_icon("folder24.png"))
                child_node.setCheckState(0, as_qt_selection(sub_folder.selected))

            render_call(update_node_data, ignore_updates=True)

        for job in folder.jobs:
            child_node = create_node(job)
            parent_node.addChild(child_node)

            def update_node_data():
                child_node.setText(0, job.name)
                child_node.setIcon(0, get_icon("job24.png"))
                child_node.setCheckState(0, as_qt_selection(job.selected))

            render_call(update_node_data, ignore_updates=True)


def create_node(item: Any):
    child_node = QTreeWidgetItem()
    child_node.setFlags(child_node.flags() | Qt.ItemIsUserCheckable)
    child_node.setCheckState(0, Qt.CheckState.Checked)
    child_node.setData(1, 0, item)

    return child_node

