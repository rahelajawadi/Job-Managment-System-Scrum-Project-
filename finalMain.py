from PyQt5 import QtCore, QtGui, QtWidgets
import finalUser


# importing admin file 

import finalAd
import Registration

class Ui_FirstWindow(object):
    def movetoUser(self):
        self.window1 = QtWidgets.QMainWindow()
        self.secondUI = finalUser.Ui_jobSeekerLogin()
        self.secondUI.setupUi(self.window1)
        self.window1.show()

	        
    def movetoAdmin(self):
        self.window2= QtWidgets.QMainWindow()
        self.adminUI= finalAd.Ui_AdminLogin()
        self.adminUI.setupUi(self.window2)
        self.window2.show()

    def movetoUserReg(self):
        self.window3 = QtWidgets.QMainWindow()
        self.regUI = Registration.Ui_jobSeekerLogin()
        self.regUI.setupUi(self.window3)
        self.window3.show()

    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("FirstWindow")
        FirstWindow.resize(1200, 750)
        FirstWindow.setStyleSheet("background-color:#fff;")
        FirstWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(FirstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(220, 220, 381, 331))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("images/images (9).jpg"))
        self.image.setScaledContents(True)
        self.image.setWordWrap(False)
        self.image.setObjectName("image")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(0, 0, 1201, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("background-color:#29A8CE;\n"
                                    "color:#f1f1f1;")
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(660, 220, 411, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblText = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.lblText.setFont(font)
        self.lblText.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lblText.setWordWrap(True)
        self.lblText.setObjectName("lblText")
        self.verticalLayout.addWidget(self.lblText)
        spacerItem = QtWidgets.QSpacerItem(27, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnAdmin = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.btnAdmin.setFont(font)
        self.btnAdmin.setObjectName("btnAdmin")
        self.horizontalLayout.addWidget(self.btnAdmin)
        spacerItem3 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.btnUser = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.btnUser.setFont(font)
        self.btnUser.setObjectName("btnUser")
        self.horizontalLayout.addWidget(self.btnUser)
        spacerItem4 = QtWidgets.QSpacerItem(24, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.lblRegister = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lblRegister.setFont(font)
        self.lblRegister.setWordWrap(True)
        self.lblRegister.setObjectName("lblRegister")
        self.horizontalLayout_2.addWidget(self.lblRegister)
        spacerItem7 = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.btnRegister = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegister.setFont(font)
        self.btnRegister.setObjectName("btnRegister")
        self.horizontalLayout_2.addWidget(self.btnRegister)
        spacerItem8 = QtWidgets.QSpacerItem(40, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        FirstWindow.setCentralWidget(self.centralwidget)
        self.btnUser.setStyleSheet('QPushButton {background-color: #29A8CE; color:#f1f1f1}')
        self.btnAdmin.setStyleSheet('QPushButton {background-color: #29A8CE; color:#f1f1f1}')
        self.btnRegister.setStyleSheet('QPushButton {background-color: #86B250; color:#f1f1f1}')

        self.retranslateUi(FirstWindow)
        QtCore.QMetaObject.connectSlotsByName(FirstWindow)

        # calling the methods using lambda expression
        # Moving to the user page in order to login themselves
        self.btnUser.clicked.connect(self.movetoUser)
        self.btnUser.clicked.connect(lambda: self.movetoUserPage(FirstWindow))

        #moving to admin page
        self.btnAdmin.clicked.connect(self.movetoAdmin)
        self.btnAdmin.clicked.connect(lambda: self.movetoAdminPage(FirstWindow))

        #moving to registration Page
        self.btnRegister.clicked.connect(self.movetoUserReg)
        self.btnRegister.clicked.connect(lambda: self.exit(FirstWindow))

    def movetoUserPage(self, FirstWindow):
        FirstWindow.hide()

    def movetoAdminPage(self, FirstWindow):
        FirstWindow.hide()

    def exit(self, FirstWindow):
        FirstWindow.hide()

    def retranslateUi(self, FirstWindow):
        _translate = QtCore.QCoreApplication.translate
        FirstWindow.setWindowTitle(_translate("FirstWindow", "Job Application Managment System"))
        self.lblTitle.setText(_translate("FirstWindow", "Employment Application Software"))
        self.lblText.setText(_translate("FirstWindow",
                                        "Recruiting candidates is easier while comming to online. Whether you work for a recruitment agency or in any other department, our cloud-based recruitment software is made for you. Start now!"))
        self.label.setText(_translate("FirstWindow", "Login As:"))
        self.btnAdmin.setText(_translate("FirstWindow", "Admin"))
        self.btnUser.setText(_translate("FirstWindow", "Job Seeker"))
        self.lblRegister.setText(_translate("FirstWindow", "Are you new? "))
        self.btnRegister.setText(_translate("FirstWindow", "Register"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FirstWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(FirstWindow)
    FirstWindow.show()
    sys.exit(app.exec_())
