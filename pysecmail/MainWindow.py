# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 0, 581, 481))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtEmailName = QtWidgets.QLineEdit(self.widget)
        self.txtEmailName.setObjectName("txtEmailName")
        self.horizontalLayout.addWidget(self.txtEmailName)
        self.cboDomain = QtWidgets.QComboBox(self.widget)
        self.cboDomain.setObjectName("cboDomain")
        self.horizontalLayout.addWidget(self.cboDomain)
        self.btnGenerateEmail = QtWidgets.QPushButton(self.widget)
        self.btnGenerateEmail.setObjectName("btnGenerateEmail")
        self.horizontalLayout.addWidget(self.btnGenerateEmail)
        self.btnAddNewEmail = QtWidgets.QPushButton(self.widget)
        self.btnAddNewEmail.setObjectName("btnAddNewEmail")
        self.horizontalLayout.addWidget(self.btnAddNewEmail)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lstEmailAddresses = QtWidgets.QListView(self.widget)
        self.lstEmailAddresses.setObjectName("lstEmailAddresses")
        self.verticalLayout.addWidget(self.lstEmailAddresses)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnCheckEmail = QtWidgets.QPushButton(self.widget)
        self.btnCheckEmail.setObjectName("btnCheckEmail")
        self.horizontalLayout_2.addWidget(self.btnCheckEmail)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lstEmails = QtWidgets.QListView(self.widget)
        self.lstEmails.setObjectName("lstEmails")
        self.verticalLayout.addWidget(self.lstEmails)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnViewEmail = QtWidgets.QPushButton(self.widget)
        self.btnViewEmail.setObjectName("btnViewEmail")
        self.horizontalLayout_3.addWidget(self.btnViewEmail)
        self.btnDeleteEmail = QtWidgets.QPushButton(self.widget)
        self.btnDeleteEmail.setObjectName("btnDeleteEmail")
        self.horizontalLayout_3.addWidget(self.btnDeleteEmail)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PySecMail"))
        self.btnGenerateEmail.setText(_translate("MainWindow", "&Generate"))
        self.btnAddNewEmail.setText(_translate("MainWindow", "&Add Email"))
        self.btnCheckEmail.setText(_translate("MainWindow", "&Check Email"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete Email Address"))
        self.btnViewEmail.setText(_translate("MainWindow", "&View Email"))
        self.btnDeleteEmail.setText(_translate("MainWindow", "&Delete Email"))
