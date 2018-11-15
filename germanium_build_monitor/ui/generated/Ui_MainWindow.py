# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui',
# licensing of 'ui/MainWindow.ui' applies.
#
# Created: Thu Nov 15 18:12:10 2018
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.current_view = QtWidgets.QVBoxLayout()
        self.current_view.setObjectName("current_view")
        self.verticalLayout.addLayout(self.current_view)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_Felix_Build_Monitor = QtWidgets.QAction(MainWindow)
        self.actionAbout_Felix_Build_Monitor.setObjectName("actionAbout_Felix_Build_Monitor")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionE_xit = QtWidgets.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.menu_File.addAction(self.actionMinimize)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionE_xit)
        self.menu_Help.addAction(self.actionAbout_Felix_Build_Monitor)
        self.menu_Help.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Felix Build Monitor", None, -1))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.menu_Help.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Help", None, -1))
        self.actionAbout_Felix_Build_Monitor.setText(QtWidgets.QApplication.translate("MainWindow", "About Felix Build Monitor", None, -1))
        self.actionAbout_Qt.setText(QtWidgets.QApplication.translate("MainWindow", "About Qt", None, -1))
        self.actionMinimize.setText(QtWidgets.QApplication.translate("MainWindow", "Minimize", None, -1))
        self.actionE_xit.setText(QtWidgets.QApplication.translate("MainWindow", "E&xit", None, -1))

