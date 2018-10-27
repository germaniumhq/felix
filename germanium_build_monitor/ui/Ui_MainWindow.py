# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui',
# licensing of 'ui/MainWindow.ui' applies.
#
# Created: Sat Oct 27 10:22:32 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_server_button = QtWidgets.QPushButton(self.layoutWidget)
        self.add_server_button.setIconSize(QtCore.QSize(24, 24))
        self.add_server_button.setObjectName("add_server_button")
        self.horizontalLayout.addWidget(self.add_server_button)
        self.add_folder_button = QtWidgets.QPushButton(self.layoutWidget)
        self.add_folder_button.setIconSize(QtCore.QSize(24, 24))
        self.add_folder_button.setObjectName("add_folder_button")
        self.horizontalLayout.addWidget(self.add_folder_button)
        self.add_job_button = QtWidgets.QPushButton(self.layoutWidget)
        self.add_job_button.setIconSize(QtCore.QSize(24, 24))
        self.add_job_button.setObjectName("add_job_button")
        self.horizontalLayout.addWidget(self.add_job_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.delete_item_button = QtWidgets.QPushButton(self.layoutWidget)
        self.delete_item_button.setIconSize(QtCore.QSize(24, 24))
        self.delete_item_button.setObjectName("delete_item_button")
        self.horizontalLayout.addWidget(self.delete_item_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeView = QtWidgets.QTreeView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.horizontalLayout_2.addWidget(self.splitter)
        self.current_view = QtWidgets.QVBoxLayout()
        self.current_view.setObjectName("current_view")
        self.horizontalLayout_2.addLayout(self.current_view)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Germanium Build Watcher", None, -1))
        self.add_server_button.setText(QtWidgets.QApplication.translate("MainWindow", "Add Server", None, -1))
        self.add_folder_button.setText(QtWidgets.QApplication.translate("MainWindow", "Add Folder", None, -1))
        self.add_job_button.setText(QtWidgets.QApplication.translate("MainWindow", "Add Job", None, -1))
        self.delete_item_button.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))

