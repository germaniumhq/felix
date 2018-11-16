# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/JenkinsBuildBranchFrame.ui',
# licensing of 'ui/JenkinsBuildBranchFrame.ui' applies.
#
# Created: Thu Nov 15 18:38:43 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 74)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(2, -1, 2, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.status_icon_label = QtWidgets.QLabel(self.frame)
        self.status_icon_label.setCursor(QtCore.Qt.ArrowCursor)
        self.status_icon_label.setObjectName("status_icon_label")
        self.horizontalLayout_4.addWidget(self.status_icon_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(2, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.project_name_label = QtWidgets.QLabel(self.frame)
        self.project_name_label.setCursor(QtCore.Qt.ArrowCursor)
        self.project_name_label.setStyleSheet("font-weight: bold")
        self.project_name_label.setObjectName("project_name_label")
        self.horizontalLayout_2.addWidget(self.project_name_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.previous_builds_container = QtWidgets.QHBoxLayout()
        self.previous_builds_container.setContentsMargins(4, -1, -1, -1)
        self.previous_builds_container.setObjectName("previous_builds_container")
        self.horizontalLayout_2.addLayout(self.previous_builds_container)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.branch_name_label = QtWidgets.QLabel(self.frame)
        self.branch_name_label.setCursor(QtCore.Qt.ArrowCursor)
        self.branch_name_label.setStyleSheet("font-style: italic")
        self.branch_name_label.setObjectName("branch_name_label")
        self.verticalLayout.addWidget(self.branch_name_label)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, 6, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.time_label = QtWidgets.QLabel(self.frame)
        self.time_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_3.addWidget(self.time_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.status_icon_label.setText(QtWidgets.QApplication.translate("Form", "icon", None, -1))
        self.project_name_label.setText(QtWidgets.QApplication.translate("Form", "project", None, -1))
        self.branch_name_label.setText(QtWidgets.QApplication.translate("Form", "branch", None, -1))
        self.time_label.setText(QtWidgets.QApplication.translate("Form", "time", None, -1))

