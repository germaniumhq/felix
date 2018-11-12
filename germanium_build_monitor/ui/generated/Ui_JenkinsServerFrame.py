# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/JenkinsServerFrame.ui',
# licensing of 'ui/JenkinsServerFrame.ui' applies.
#
# Created: Mon Nov 12 05:52:56 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.server_name_label = QtWidgets.QLabel(Form)
        self.server_name_label.setObjectName("server_name_label")
        self.verticalLayout.addWidget(self.server_name_label)
        self.content = QtWidgets.QGridLayout()
        self.content.setObjectName("content")
        self.verticalLayout.addLayout(self.content)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.server_name_label.setText(QtWidgets.QApplication.translate("Form", "server name", None, -1))

