
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import finalMain


class Ui_AdminLogin(object):



    def returnToMain(self):
        self.window1 = QtWidgets.QMainWindow()
        self.secondUI = finalMain.Ui_FirstWindow()
        self.secondUI.setupUi(self.window1)
        self.window1.show()

    def setupUi(self, AdminLogin):
        AdminLogin.setObjectName("AdminLogin")
        AdminLogin.resize(1150, 700)
        AdminLogin.setStyleSheet("background-color:#fff;")
        self.centralwidget = QtWidgets.QWidget(AdminLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 200, 361, 381))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.userbame = QtWidgets.QLineEdit(self.groupBox)
        self.userbame.setGeometry(QtCore.QRect(140, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.userbame.setFont(font)
        self.userbame.setObjectName("userbame")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(140, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(self.groupBox)
        self.login.setGeometry(QtCore.QRect(220, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setStyleSheet("background-color: #29A8CE;\n"
"border:none;\n"
"color:#fff;\n"
"")
        self.login.setObjectName("login")
        self.cancel = QtWidgets.QPushButton(self.groupBox)
        self.cancel.setGeometry(QtCore.QRect(140, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("background-color: #105687;\n"
"border:none;\n"
"color:#fff;\n"
"")
        self.cancel.setObjectName("cancel")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(0, 0, 1200, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("background-color: #105687;\n"
"border:none;\n"
"color:#fff;")
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 210, 461, 361))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/images (3).jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        AdminLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminLogin)
        QtCore.QMetaObject.connectSlotsByName(AdminLogin)

    def retranslateUi(self, AdminLogin):
        _translate = QtCore.QCoreApplication.translate
        AdminLogin.setWindowTitle(_translate("AdminLogin", "MainWindow"))
        self.groupBox.setTitle(_translate("AdminLogin", "Welcome to Admin Login Form"))
        self.label.setText(_translate("AdminLogin", "Username"))
        self.label_2.setText(_translate("AdminLogin", "Password"))
        self.login.setText(_translate("AdminLogin", "login"))
        self.cancel.setText(_translate("AdminLogin", "cancel"))
        self.lblTitle.setText(_translate("AdminLogin", "Employment Application Software"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminLogin = QtWidgets.QMainWindow()
    ui = Ui_AdminLogin()
    ui.setupUi(AdminLogin)
    AdminLogin.show()
    sys.exit(app.exec_())
