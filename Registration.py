
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import finalMain


class Ui_jobSeekerLogin(object):
    def returnToMain(self):
        self.window1 = QtWidgets.QMainWindow()
        self.secondUI = finalMain.Ui_FirstWindow()
        self.secondUI.setupUi(self.window1)
        self.window1.show()
    def setupUi(self, jobSeekerLogin):
        jobSeekerLogin.setObjectName("jobSeekerLogin")
        jobSeekerLogin.resize(1200, 750)
        jobSeekerLogin.setStyleSheet("background-color:#fff;")
        jobSeekerLogin.setDockNestingEnabled(False)
        jobSeekerLogin.setStyleSheet("QWidget  #facebook{\n"
"background-color: #105687;\n"
"border:none;\n"
"color:#fff;\n"
"}\n"
"\n"
"QWidget  #twitter{\n"
"background-color: #54A0FB;\n"
"border:none;\n"
"color:#fff;\n"
"}\n"
"\n"
"QWidget  #whatsapp{\n"
"background-color: #41CD52;\n"
"border:none;\n"
"color:#fff;\n"
"}\n"
"\n"
"QWidget  #Instagram{\n"
"background-color: #105687;\n"
"border:none;\n"
"color:#fff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(jobSeekerLogin)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(150, 170, 521, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.userbame = QtWidgets.QLineEdit(self.groupBox)
        self.userbame.setGeometry(QtCore.QRect(40, 120, 185, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.userbame.setFont(font)
        self.userbame.setObjectName("userbame")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(40, 180, 187, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.btn_reg = QtWidgets.QPushButton(self.groupBox)
        self.btn_reg.setGeometry(QtCore.QRect(390, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reg.setFont(font)
        self.btn_reg.setStyleSheet("background-color: #5AAA78;\n"
"border:none;\n"
"color:#fff;\n"
"")
        self.btn_reg.setObjectName("btn_reg")
        self.cancel = QtWidgets.QPushButton(self.groupBox)
        self.cancel.setGeometry(QtCore.QRect(290, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("background-color: #105687;\n"
"border:none;\n"
"color:#fff;")
        self.cancel.setObjectName("cancel")
        self.email = QtWidgets.QLineEdit(self.groupBox)
        self.email.setGeometry(QtCore.QRect(280, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.phone = QtWidgets.QLineEdit(self.groupBox)
        self.phone.setGeometry(QtCore.QRect(280, 120, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.phone.setFont(font)
        self.phone.setObjectName("phone")
        self.name = QtWidgets.QLineEdit(self.groupBox)
        self.name.setGeometry(QtCore.QRect(40, 70, 182, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(280, 180, 191, 31))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(40, 250, 281, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(0, 0, 1201, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("background-color: #5AAA78;\n"
"border:none;\n"
"color:#fff;")
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(760, 140, 391, 461))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.facebook = QtWidgets.QPushButton(self.frame_2)
        self.facebook.setGeometry(QtCore.QRect(70, 80, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.facebook.setFont(font)
        self.facebook.setObjectName("facebook")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(60, 15, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.twitter = QtWidgets.QPushButton(self.frame_2)
        self.twitter.setGeometry(QtCore.QRect(70, 170, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.twitter.setFont(font)
        self.twitter.setObjectName("twitter")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 350, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"background-color: #105687;\n"
"border:none;\n"
"color:#fff;\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet('QPushButton {background-color: #FF4657; color: #fff}')
        self.whatsapp = QtWidgets.QPushButton(self.frame_2)
        self.whatsapp.setGeometry(QtCore.QRect(70, 260, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.whatsapp.setFont(font)
        self.whatsapp.setObjectName("whatsapp")
        jobSeekerLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(jobSeekerLogin)
        QtCore.QMetaObject.connectSlotsByName(jobSeekerLogin)
        # calling the methods
        self.cancel.clicked.connect(self.returnToMain)
        self.cancel.clicked.connect(lambda: self.closer(jobSeekerLogin))

    def closer(self, jobSeekerLogin):
            jobSeekerLogin.hide()


    def retranslateUi(self, jobSeekerLogin):
        _translate = QtCore.QCoreApplication.translate
        jobSeekerLogin.setWindowTitle(_translate("jobSeekerLogin", "MainWindow"))
        self.groupBox.setTitle(_translate("jobSeekerLogin", "Job Seekers\' Regestration Form"))
        self.userbame.setPlaceholderText(_translate("jobSeekerLogin", "Username"))
        self.password.setPlaceholderText(_translate("jobSeekerLogin", "Password"))
        self.btn_reg.setText(_translate("jobSeekerLogin", "Register"))
        self.cancel.setText(_translate("jobSeekerLogin", "cancel"))
        self.email.setPlaceholderText(_translate("jobSeekerLogin", "email"))
        self.phone.setPlaceholderText(_translate("jobSeekerLogin", "phone"))
        self.name.setPlaceholderText(_translate("jobSeekerLogin", "Name"))
        self.comboBox.setItemText(0, _translate("jobSeekerLogin", "Gender"))
        self.comboBox.setItemText(1, _translate("jobSeekerLogin", "Male"))
        self.comboBox.setItemText(2, _translate("jobSeekerLogin", "Female"))
        self.comboBox.setItemText(3, _translate("jobSeekerLogin", "Other"))
        self.checkBox.setText(_translate("jobSeekerLogin", "I have read all info  about the rules"))
        self.lblTitle.setText(_translate("jobSeekerLogin", "Welocme to Employment Application Software"))
        self.facebook.setText(_translate("jobSeekerLogin", "Facebook"))
        self.label.setText(_translate("jobSeekerLogin", "Join Us In:"))
        self.twitter.setText(_translate("jobSeekerLogin", "Twitter"))
        self.pushButton_4.setText(_translate("jobSeekerLogin", "Instagram"))
        self.whatsapp.setText(_translate("jobSeekerLogin", "Whatsapp"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jobSeekerLogin = QtWidgets.QMainWindow()
    ui = Ui_jobSeekerLogin()
    ui.setupUi(jobSeekerLogin)
    jobSeekerLogin.show()
    sys.exit(app.exec_())
