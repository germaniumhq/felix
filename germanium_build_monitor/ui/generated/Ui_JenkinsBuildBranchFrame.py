# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/JenkinsBuildBranchFrame.ui',
# licensing of 'ui/JenkinsBuildBranchFrame.ui' applies.
#
# Created: Mon Nov 12 09:35:02 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 74)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.status_icon_label = QtWidgets.QLabel(Form)
        self.status_icon_label.setObjectName("status_icon_label")
        self.horizontalLayout_2.addWidget(self.status_icon_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.project_name_label = QtWidgets.QLabel(Form)
        self.project_name_label.setObjectName("project_name_label")
        self.verticalLayout.addWidget(self.project_name_label)
        self.branch_name_label = QtWidgets.QLabel(Form)
        self.branch_name_label.setObjectName("branch_name_label")
        self.verticalLayout.addWidget(self.branch_name_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.previous_builds_container = QtWidgets.QHBoxLayout()
        self.previous_builds_container.setObjectName("previous_builds_container")
        self.horizontalLayout_3.addLayout(self.previous_builds_container)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.time_label = QtWidgets.QLabel(Form)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_3.addWidget(self.time_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.status_icon_label.setText(QtWidgets.QApplication.translate("Form", "icon", None, -1))
        self.project_name_label.setText(QtWidgets.QApplication.translate("Form", "project", None, -1))
        self.branch_name_label.setText(QtWidgets.QApplication.translate("Form", "branch", None, -1))
        self.time_label.setText(QtWidgets.QApplication.translate("Form", "time", None, -1))

