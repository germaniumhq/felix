# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AddJobDialog.ui',
# licensing of 'ui/AddJobDialog.ui' applies.
#
# Created: Sat Oct 27 05:30:37 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 414)
        Dialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.monitored_branches_table = QtWidgets.QTableView(Dialog)
        self.monitored_branches_table.setObjectName("monitored_branches_table")
        self.horizontalLayout.addWidget(self.monitored_branches_table)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.branch_move_up_button = QtWidgets.QToolButton(Dialog)
        self.branch_move_up_button.setObjectName("branch_move_up_button")
        self.verticalLayout.addWidget(self.branch_move_up_button)
        self.branch_move_down_button = QtWidgets.QToolButton(Dialog)
        self.branch_move_down_button.setObjectName("branch_move_down_button")
        self.verticalLayout.addWidget(self.branch_move_down_button)
        self.branch_edit_button = QtWidgets.QToolButton(Dialog)
        self.branch_edit_button.setObjectName("branch_edit_button")
        self.verticalLayout.addWidget(self.branch_edit_button)
        self.branch_add_before_button = QtWidgets.QToolButton(Dialog)
        self.branch_add_before_button.setObjectName("branch_add_before_button")
        self.verticalLayout.addWidget(self.branch_add_before_button)
        self.branch_add_after_button = QtWidgets.QToolButton(Dialog)
        self.branch_add_after_button.setObjectName("branch_add_after_button")
        self.verticalLayout.addWidget(self.branch_add_after_button)
        self.branch_delete_button = QtWidgets.QToolButton(Dialog)
        self.branch_delete_button.setObjectName("branch_delete_button")
        self.verticalLayout.addWidget(self.branch_delete_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cancel_dialog_button = QtWidgets.QPushButton(Dialog)
        self.cancel_dialog_button.setObjectName("cancel_dialog_button")
        self.horizontalLayout_2.addWidget(self.cancel_dialog_button)
        self.add_job_button = QtWidgets.QPushButton(Dialog)
        self.add_job_button.setObjectName("add_job_button")
        self.horizontalLayout_2.addWidget(self.add_job_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Add Job", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Name", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "URL", None, -1))
        self.lineEdit_2.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "/job/job-name/", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("Dialog", "Include in the systray list", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "Branches <span style=\"color:lightgray\">(regex)</span>", None, -1))
        self.branch_move_up_button.setText(QtWidgets.QApplication.translate("Dialog", "...", None, -1))
        self.branch_move_down_button.setText(QtWidgets.QApplication.translate("Dialog", "...", None, -1))
        self.branch_edit_button.setText(QtWidgets.QApplication.translate("Dialog", "...", None, -1))
        self.branch_add_before_button.setText(QtWidgets.QApplication.translate("Dialog", "...", None, -1))
        self.branch_add_after_button.setText(QtWidgets.QApplication.translate("Dialog", "...", None, -1))
        self.branch_delete_button.setText(QtWidgets.QApplication.translate("Dialog", "...", None, -1))
        self.cancel_dialog_button.setText(QtWidgets.QApplication.translate("Dialog", "Cancel", None, -1))
        self.add_job_button.setText(QtWidgets.QApplication.translate("Dialog", "Add", None, -1))

