# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AddBranchDialog.ui',
# licensing of 'ui/AddBranchDialog.ui' applies.
#
# Created: Sat Nov  3 04:30:26 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(566, 433)
        Dialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtWidgets.QPushButton(Dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.add_button = QtWidgets.QPushButton(Dialog)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 2, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.action_monitor_radio_button = QtWidgets.QRadioButton(self.groupBox_2)
        self.action_monitor_radio_button.setChecked(True)
        self.action_monitor_radio_button.setObjectName("action_monitor_radio_button")
        self.verticalLayout_2.addWidget(self.action_monitor_radio_button)
        self.action_ignore_radio_button = QtWidgets.QRadioButton(self.groupBox_2)
        self.action_ignore_radio_button.setObjectName("action_ignore_radio_button")
        self.verticalLayout_2.addWidget(self.action_ignore_radio_button)
        self.gridLayout.addWidget(self.groupBox_2, 4, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.notification_never_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.notification_never_radio_button.setObjectName("notification_never_radio_button")
        self.verticalLayout.addWidget(self.notification_never_radio_button)
        self.notification_state_change_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.notification_state_change_radio_button.setChecked(True)
        self.notification_state_change_radio_button.setObjectName("notification_state_change_radio_button")
        self.verticalLayout.addWidget(self.notification_state_change_radio_button)
        self.notification_each_build_radio_button = QtWidgets.QRadioButton(self.groupBox)
        self.notification_each_build_radio_button.setObjectName("notification_each_build_radio_button")
        self.verticalLayout.addWidget(self.notification_each_build_radio_button)
        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.action_monitor_radio_button)
        Dialog.setTabOrder(self.action_monitor_radio_button, self.action_ignore_radio_button)
        Dialog.setTabOrder(self.action_ignore_radio_button, self.notification_never_radio_button)
        Dialog.setTabOrder(self.notification_never_radio_button, self.notification_state_change_radio_button)
        Dialog.setTabOrder(self.notification_state_change_radio_button, self.notification_each_build_radio_button)
        Dialog.setTabOrder(self.notification_each_build_radio_button, self.add_button)
        Dialog.setTabOrder(self.add_button, self.cancel_button)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Add Branch", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Test", None, -1))
        self.cancel_button.setText(QtWidgets.QApplication.translate("Dialog", "Cancel", None, -1))
        self.add_button.setText(QtWidgets.QApplication.translate("Dialog", "Add", None, -1))
        self.lineEdit_2.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "/feature/some-branch-name", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "RegEx <span style=\"color: red\">*</span>", None, -1))
        self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", ".*", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p>When will the system notifications be triggered. These will be considered only if the branch is being processed.</p></body></html>", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Dialog", "Action", None, -1))
        self.action_monitor_radio_button.setText(QtWidgets.QApplication.translate("Dialog", "Monitor", None, -1))
        self.action_ignore_radio_button.setText(QtWidgets.QApplication.translate("Dialog", "I&gnore", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "<span style=\"color:green\">matches</span>", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p>What will happen if the name matches. If the action is set to &quot;Monitor&quot;, it is included in the Job status.</p></body></html>", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dialog", "Notification", None, -1))
        self.notification_never_radio_button.setText(QtWidgets.QApplication.translate("Dialog", "&Never", None, -1))
        self.notification_state_change_radio_button.setText(QtWidgets.QApplication.translate("Dialog", "On Change", None, -1))
        self.notification_each_build_radio_button.setText(QtWidgets.QApplication.translate("Dialog", "Alwa&ys", None, -1))

