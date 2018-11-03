# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AddFolderDialog.ui',
# licensing of 'ui/AddFolderDialog.ui' applies.
#
# Created: Sat Nov  3 04:30:26 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 130)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.checkBox)
        Dialog.setTabOrder(self.checkBox, self.pushButton_2)
        Dialog.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Add Folder...", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Name <span style=\"color: red\">*</span>", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("Dialog", "Include in systray list", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Dialog", "Close", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Dialog", "Add", None, -1))

