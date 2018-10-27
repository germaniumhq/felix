from typing import Dict
import os

from PySide2 import QtGui

from germanium_build_monitor.resources import base_dir


icon_cache: Dict[str, QtGui.QIcon] = dict()


def get_icon(icon_name: str) -> QtGui.QIcon:
    if icon_name in icon_cache:
        return icon_cache[icon_name]

    icon = create_icon(icon_name)

    icon_cache[icon_name] = icon

    return icon


def create_icon(icon_name: str) -> QtGui.QIcon:
    icon = QtGui.QIcon()
    icon_path = os.path.join(base_dir(), icon_name)

    icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    return icon

