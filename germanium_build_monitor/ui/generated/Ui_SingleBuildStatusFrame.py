# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SingleBuildStatusFrame.ui',
# licensing of 'ui/SingleBuildStatusFrame.ui' applies.
#
# Created: Mon Nov 12 09:35:02 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(114, 42)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.build_status_label = QtWidgets.QLabel(Form)
        self.build_status_label.setObjectName("build_status_label")
        self.horizontalLayout.addWidget(self.build_status_label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.build_status_label.setText(QtWidgets.QApplication.translate("Form", "build_status", None, -1))

