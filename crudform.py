# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pythonprojects\CRUDpyqt4\crudform.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(629, 403)
        MainWindow.setWindowIcon(QtGui.QIcon('favicon.png'))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.name = QtGui.QLineEdit(self.tab)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout_2.addWidget(self.name, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei UI"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.username = QtGui.QLineEdit(self.tab)
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout_2.addWidget(self.username, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei UI"))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei UI"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.password = QtGui.QLineEdit(self.tab)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout_2.addWidget(self.password, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei UI"))
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)
        self.confirm = QtGui.QLineEdit(self.tab)
        self.confirm.setObjectName(_fromUtf8("confirm"))
        self.gridLayout_2.addWidget(self.confirm, 3, 2, 1, 1)
        self.registerbtn = QtGui.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Maiandra GD"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.registerbtn.setFont(font)
        self.registerbtn.setAutoFillBackground(False)
        self.registerbtn.setObjectName(_fromUtf8("registerbtn"))
        self.gridLayout_2.addWidget(self.registerbtn, 4, 1, 1, 2)
        self.tabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei UI"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.username2 = QtGui.QLineEdit(self.tab_2)
        self.username2.setObjectName(_fromUtf8("username2"))
        self.gridLayout_4.addWidget(self.username2, 0, 1, 1, 1)
        self.frame = QtGui.QFrame(self.tab_2)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_9 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei UI"))
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.idx = QtGui.QLineEdit(self.frame)
        self.idx.setObjectName(_fromUtf8("idx"))
        self.gridLayout_3.addWidget(self.idx, 1, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei UI"))
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 2)
        self.passx = QtGui.QLineEdit(self.frame)
        self.passx.setObjectName(_fromUtf8("passx"))
        self.gridLayout_3.addWidget(self.passx, 2, 2, 1, 1)
        self.searchx = QtGui.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Maiandra GD"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchx.setFont(font)
        self.searchx.setAutoFillBackground(False)
        self.searchx.setObjectName(_fromUtf8("searchx"))
        self.gridLayout_3.addWidget(self.searchx, 3, 1, 1, 2)
        self.gridLayout_4.addWidget(self.frame, 0, 2, 3, 1)
        self.label_8 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei UI"))
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)
        self.name2 = QtGui.QLineEdit(self.tab_2)
        self.name2.setObjectName(_fromUtf8("name2"))
        self.gridLayout_4.addWidget(self.name2, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei UI"))
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)
        self.password2 = QtGui.QLineEdit(self.tab_2)
        self.password2.setObjectName(_fromUtf8("password2"))
        self.gridLayout_4.addWidget(self.password2, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft JhengHei UI"))
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)
        self.confirm2 = QtGui.QLineEdit(self.tab_2)
        self.confirm2.setObjectName(_fromUtf8("confirm2"))
        self.gridLayout_4.addWidget(self.confirm2, 3, 1, 1, 1)
        self.updatebtn = QtGui.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Maiandra GD"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.updatebtn.setFont(font)
        self.updatebtn.setAutoFillBackground(False)
        self.updatebtn.setObjectName(_fromUtf8("updatebtn"))
        self.gridLayout_4.addWidget(self.updatebtn, 4, 1, 1, 1)
        self.cancelbtn = QtGui.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Maiandra GD"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancelbtn.setFont(font)
        self.cancelbtn.setAutoFillBackground(False)
        self.cancelbtn.setObjectName(_fromUtf8("cancelbtn"))
        self.gridLayout_4.addWidget(self.cancelbtn, 5, 1, 1, 1)
        self.tabs.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CRUD with Python and MySQL", None))
        self.label.setText(_translate("MainWindow", "Username:", None))
        self.label_4.setText(_translate("MainWindow", "Password:", None))
        self.label_3.setText(_translate("MainWindow", "Name:", None))
        self.label_5.setText(_translate("MainWindow", "Confirm", None))
        self.registerbtn.setText(_translate("MainWindow", "Register", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("MainWindow", "Register", None))
        self.label_2.setText(_translate("MainWindow", "Username:", None))
        self.label_9.setText(_translate("MainWindow", "Search ID", None))
        self.label_10.setText(_translate("MainWindow", "ID:", None))
        self.label_11.setText(_translate("MainWindow", "Password:", None))
        self.searchx.setText(_translate("MainWindow", "Search", None))
        self.label_8.setText(_translate("MainWindow", "Name:", None))
        self.label_7.setText(_translate("MainWindow", "Password:", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>Confirm:</p></body></html>", None))
        self.updatebtn.setText(_translate("MainWindow", "Update", None))
        self.cancelbtn.setText(_translate("MainWindow", "Cancel", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("MainWindow", "Configure", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

