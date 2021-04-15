
from PyQt5 import QtCore, QtGui, QtWidgets
import finalMain
import UserJobTable

class Ui_jobSeekerLogin(object):
    def setupUi(self, jobSeekerLogin):
        jobSeekerLogin.setObjectName("jobSeekerLogin")
        jobSeekerLogin.resize(1200, 750)
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
        self.frame_2.setGeometry(QtCore.QRect(20, 160, 1031, 571))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(160, 20, 240, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/best.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(160, 160, 240, 60))
        self.pushButton.setStyleSheet("background-color:#fff;\n"
"border:none;")
        self.pushButton.setObjectName("pushButton")

        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(470, 20, 240, 141))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/label3.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(780, 20, 240, 141))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("images/mypic.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(780, 280, 240, 141))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/images (8).jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 160, 240, 60))
        self.pushButton_2.setStyleSheet("background-color:#fff;\n"
"border:none;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 160, 240, 60))
        self.pushButton_3.setStyleSheet("background-color:#fff;\n"
"border:none;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 420, 240, 60))
        self.pushButton_4.setStyleSheet("background-color:#fff;\n"
"border:none;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(160, 280, 240, 141))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("images/download.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 420, 240, 60))
        self.pushButton_7.setStyleSheet("background-color:#fff;\n"
"border:none;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(480, 420, 240, 60))
        self.pushButton_6.setStyleSheet("background-color:#fff;\n"
"border:none;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(480, 280, 240, 141))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("images/resume.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(940, 114, 100, 35))
        self.btn_back.setStyleSheet("background-color: #5AAA78;\n"
                                    "border:none;\n"
                                    "color:#fff;")
        self.btn_back.setObjectName("btn_back")
        jobSeekerLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(jobSeekerLogin)
        QtCore.QMetaObject.connectSlotsByName(jobSeekerLogin)

        # Calling the methods
        self.btn_back.clicked.connect(lambda: self.closer(jobSeekerLogin))
        self.btn_back.clicked.connect(self.returnToMain)
        self.pushButton_2.clicked.connect(self.moveToUserTable)
        self.pushButton_2.clicked.connect(lambda: self.closer(jobSeekerLogin))

    def returnToMain(self):
        self.window1 = QtWidgets.QMainWindow()
        self.secondUI = finalMain.Ui_FirstWindow()
        self.secondUI.setupUi(self.window1)
        self.window1.show()

    def closer(self, jobSeekerLogin):
        jobSeekerLogin.hide()

    def moveToUserTable(self):
        self.window1 = QtWidgets.QMainWindow()
        self.secondUI = UserJobTable.Ui_UserTable()
        self.secondUI.setupUi(self.window1)
        self.window1.show()

    def retranslateUi(self, jobSeekerLogin):
        _translate = QtCore.QCoreApplication.translate
        jobSeekerLogin.setWindowTitle(_translate("jobSeekerLogin", "MainWindow"))
        self.lblTitle.setText(_translate("jobSeekerLogin", "Welocme to Employment Application Software"))
        self.pushButton.setText(_translate("jobSeekerLogin", "My Profile"))
        self.pushButton_2.setText(_translate("jobSeekerLogin", "View Jobs"))
        self.pushButton_3.setText(_translate("jobSeekerLogin", "Approved Applications"))
        self.pushButton_4.setText(_translate("jobSeekerLogin", "Need Help"))
        self.pushButton_7.setText(_translate("jobSeekerLogin", "My Card"))
        self.pushButton_6.setText(_translate("jobSeekerLogin", "Update Resume"))
        self.btn_back.setText(_translate("jobSeekerLogin", "logout"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jobSeekerLogin = QtWidgets.QMainWindow()
    ui = Ui_jobSeekerLogin()
    ui.setupUi(jobSeekerLogin)
    jobSeekerLogin.show()
    sys.exit(app.exec_())
