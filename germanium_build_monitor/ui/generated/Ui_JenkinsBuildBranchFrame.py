# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/JenkinsBuildBranchFrame.ui',
# licensing of 'ui/JenkinsBuildBranchFrame.ui' applies.
#
# Created: Mon Nov 12 06:20:13 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(317, 160)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.project_name_label = QtWidgets.QLabel(Form)
        self.project_name_label.setObjectName("project_name_label")
        self.verticalLayout.addWidget(self.project_name_label)
        self.branch_name_label = QtWidgets.QLabel(Form)
        self.branch_name_label.setObjectName("branch_name_label")
        self.verticalLayout.addWidget(self.branch_name_label)
        self.build_status_label = QtWidgets.QLabel(Form)
        self.build_status_label.setObjectName("build_status_label")
        self.verticalLayout.addWidget(self.build_status_label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.project_name_label.setText(QtWidgets.QApplication.translate("Form", "project", None, -1))
        self.branch_name_label.setText(QtWidgets.QApplication.translate("Form", "branch", None, -1))
        self.build_status_label.setText(QtWidgets.QApplication.translate("Form", "build status", None, -1))

