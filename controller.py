from PyQt4 import QtGui
import sys
import crudform
import model

class MainWindow(QtGui.QMainWindow, crudform.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setMaximumSize(629, 403)

        # button events
        self.registerbtn.clicked.connect(self.insertdatatomodel)
        self.searchx.clicked.connect(self.finduser)
        self.updatebtn.clicked.connect(self.updateuser)
        self.cancelbtn.clicked.connect(lambda: self.clear(self.username2, self.password2, self.name2, self.confirm2))

        # widgets' configurations
        self.username.setMaxLength(20)
        self.name.setMaxLength(50)
        self.password.setMaxLength(50)
        self.confirm.setMaxLength(50)
        self.username2.setMaxLength(20)
        self.name2.setMaxLength(50)
        self.password2.setMaxLength(50)
        self.confirm2.setMaxLength(50)
        self.username2.setReadOnly(True)
        self.name2.setReadOnly(True)
        self.password2.setReadOnly(True)
        self.confirm2.setReadOnly(True)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.confirm.setEchoMode(QtGui.QLineEdit.Password)
        self.password2.setEchoMode(QtGui.QLineEdit.Password)
        self.confirm2.setEchoMode(QtGui.QLineEdit.Password)
        self.updatebtn.setEnabled(False)
        self.cancelbtn.setEnabled(False)

        self.show()

    def clear(self, a, b, c, d):
        a.setText('')
        b.setText('')
        c.setText('')
        d.setText('')

    def enabledtext(self, a, b, c, d):
        a.setReadOnly(False)
        b.setReadOnly(False)
        c.setReadOnly(False)
        d.setReadOnly(False)

    def insertdatatomodel(self):
        x = model.Db((self.username.text(),
                         self.name.text(),
                         self.password.text(),
                         self.confirm.text()))
        try:
            x = x.insertdata()
            if x[0] is not True:
                QtGui.QMessageBox.warning(self, 'error 101', x, None)
            else:
                QtGui.QMessageBox.information(self, 'success', 'Registered Man\nYour ID is: ' + str(x[1]), None)
                self.clear(self.username, self.password, self.name, self.confirm)
        except:
            QtGui.QMessageBox.warning(self, 'Database Error', 'Not Connected', None)

    def finduser(self):
        x = model.Db((self.idx.text(),
                     self.passx.text()))
        try:
            x = x.searchuser()
            if x[0] is not True:
                QtGui.QMessageBox.warning(self, 'error 101', x, None)
            else:
                self.username2.setText(x[1][0])
                self.name2.setText(x[1][2])
                self.enabledtext(self.username2, self.password2, self.name2, self.confirm2)
                self.updatebtn.setEnabled(True)
                self.cancelbtn.setEnabled(True)
        except:
            QtGui.QMessageBox.warning(self, 'Database Error', 'Not Connected', None)

    def updateuser(self):
        x = model.Db((self.username2.text(),
                     self.name2.text(),
                     self.password2.text(),
                     self.confirm2.text()))
        try:
            x = x.updateinfos()
            if x is not True:
                QtGui.QMessageBox.warning(self, 'error 101', x, None)
            else:
                QtGui.QMessageBox.information(self, 'success', 'Infos are successfully updated', None)
        except:
            QtGui.QMessageBox.warning(self, 'Database Error', 'Not Connected', None)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = MainWindow()
    app.setStyle(QtGui.QStyleFactory.create('plastique'))
    sys.exit(app.exec_())
