# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/sunxinyu/Workspace/face/ui/formWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.button1 = QtWidgets.QPushButton(Form)
        self.button1.setGeometry(QtCore.QRect(235, 265, 80, 30))
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(Form)
        self.button2.setGeometry(QtCore.QRect(310, 265, 80, 30))
        self.button2.setObjectName("button2")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 30, 361, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 361, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "All Users"))
        self.button1.setText(_translate("Form", "remove"))
        self.button2.setText(_translate("Form", "save"))
        self.lineEdit.setText(_translate("Form", "Search"))
