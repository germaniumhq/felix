# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/JobBranchView.ui',
# licensing of 'ui/JobBranchView.ui' applies.
#
# Created: Mon Oct 29 18:18:54 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(751, 567)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(Frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.job_name_label = QtWidgets.QLabel(Frame)
        self.job_name_label.setTextFormat(QtCore.Qt.RichText)
        self.job_name_label.setObjectName("job_name_label")
        self.verticalLayout.addWidget(self.job_name_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.branch_filter_input = QtWidgets.QLineEdit(Frame)
        self.branch_filter_input.setObjectName("branch_filter_input")
        self.horizontalLayout.addWidget(self.branch_filter_input)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.edit_button = QtWidgets.QPushButton(Frame)
        self.edit_button.setObjectName("edit_button")
        self.horizontalLayout.addWidget(self.edit_button)
        self.view_site_button = QtWidgets.QPushButton(Frame)
        self.view_site_button.setObjectName("view_site_button")
        self.horizontalLayout.addWidget(self.view_site_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(Frame)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QtWidgets.QApplication.translate("Frame", "Frame", None, -1))
        self.job_name_label.setText(QtWidgets.QApplication.translate("Frame", "<b>Job Name</b>", None, -1))
        self.branch_filter_input.setPlaceholderText(QtWidgets.QApplication.translate("Frame", "filter branches", None, -1))
        self.edit_button.setText(QtWidgets.QApplication.translate("Frame", "Edit", None, -1))
        self.view_site_button.setText(QtWidgets.QApplication.translate("Frame", "View in Jenkins", None, -1))

