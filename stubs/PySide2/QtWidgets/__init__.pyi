from typing import Optional, List, Union, Any
from PySide2.QtCore import QEvent, Qt
from PySide2.QtGui import QIcon


class QObject:
    pass


class QWidget:
    def deleteLater(self):
        pass


class QLayout:
    def addWidget(self, widget: QWidget):
        pass

    def removeWidget(self, widget: QWidget):
        pass


class QTreeWidgetItem:
    def setFlags(self, flags: int) -> None:
        pass

    def flags(self) -> int:
        pass

    def setCheckState(self, column_index: int, state: Qt.CheckState):
        pass

    def setData(self, column_index: int, role: int, data: Any) -> None:
        pass

    def data(self, column_index):
        pass


class QSystemTrayIcon:
    def show(self) -> None:
        pass

    def hide(self) -> None:
        pass

    def setIcon(self, icon: QIcon) -> None:
        pass

    def setContextMenu(self, menu: 'QMenu') -> None:
        pass

    def setToolTip(self, tooltip: str) -> None:
        pass

    def showMessage(self,
                    title: str,
                    messag: str,
                    icon_or_timeout: Optional[Union[QIcon, int]] = None,
                    timeout: Optional[int] = None) -> None:
        pass

    @staticmethod
    def isSystemTrayAvailable() -> bool:
        pass


class QDialog:
    def __init__(self,
                 parent: Optional['QDialog'] = None):
        self.modal: bool
        self.sizeGripEnabled: bool

    def show(self) -> None:
        pass

    def hide(self) -> None:
        pass

    def setWindowTitle(self, title: str) -> None:
        pass

    def setWindowIcon(self, icon: QIcon) -> None:
        pass

    def tr(self, text: str) -> str:
        pass


class QMainWindow(QDialog):
    pass


class QApplication:

    def __init__(self, args: List[str]) -> None:
        self.focusChanged: QEvent
        pass

    def exec_(self) -> int:
        pass


class QLabel(QWidget):
    def __init__(self,
                 label: Optional[str] = "") -> None:
        pass

    def setText(self, text: str) -> None:
        pass


class QButton(QWidget):
    pass


class QAction:
    def __init__(self,
                 icon_text_or_parent: Union[QIcon, str, Optional[QObject]],
                 text_or_parent: Union[QIcon, str, Optional[QObject]] = None,
                 parent_menu: Optional[QObject] = None) -> None:
        self.triggered: QEvent


class QMenu:
    def __init__(self,
                 title_or_parent: Union[Optional[QWidget], str] = None,
                 parent: Optional[QWidget] = None) -> None:
        pass

    def addAction(self,
                  action_icon_or_title: Union['QAction', QIcon, str],
                  icon_or_title: Optional[Union[QIcon, str]] = None,
                  title: Optional[str] = None) -> QAction:
        pass

    def addSeparator(self) -> None:
        pass


class QMessageBox(QDialog):
    def __init__(self) -> None:
        self.Close: int
        self.Ignore: int
        self.Critical: int

    def exec_(self) -> int:
        pass

    def setText(self, text: str) -> None:
        pass

    def setDetailedText(self, text: str) -> None:
        pass

    def setIcon(self, icon_id: int) -> None:
        pass

    def setStandardButtons(self, button_id: int) -> None:
        pass

    def setEscapeButton(self, button_id: int) -> None:
        pass

    def setDefaultButton(self, button_id: int) -> None:
        pass

    @staticmethod
    def critical(parent: QDialog,
                 title: str,
                 description: str,
                 button_ids: int) -> None:
        pass

