

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox



class Ui_addCV(object):
    def setupUi(self, addCV):
        addCV.setObjectName("addCV")
        addCV.resize(1200, 750)
        addCV.setStyleSheet("\n"
"\n"
"\n"
"QWidget #logout{\n"
"background-color:#3A75A8;\n"
"color:#fff;\n"
"}\n"
"\n"
"QWidget #btn_apply{\n"
"background-color: #5AAA78;\n"
"color:#f1f1f1;\n"
"}\n"
"\n"
"QWidget #btn_search{\n"
"background-color: #FB8739;\n"
"color:#f1f1f1;\n"
"}\n"
"\n"
"")
        addCV.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(addCV)
        self.centralwidget.setObjectName("centralwidget")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1030, 80, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.logout.setFont(font)
        self.logout.setObjectName("logout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(4, -1, 1191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #5AAA78;\n"
"border:none;\n"
"color:#fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_apply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_apply.setGeometry(QtCore.QRect(80, 100, 71, 41))
        self.btn_apply.setObjectName("btn_apply")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(73, 180, 1041, 461))
        self.plainTextEdit.setObjectName("plainTextEdit")
        addCV.setCentralWidget(self.centralwidget)

        self.retranslateUi(addCV)
        QtCore.QMetaObject.connectSlotsByName(addCV)



    def retranslateUi(self, addCV):
        _translate = QtCore.QCoreApplication.translate
        addCV.setWindowTitle(_translate("addCV", "tableWindow"))
        self.logout.setText(_translate("addCV", "Exit"))
        self.label.setText(_translate("addCV", "Job Application Managment System"))
        self.btn_apply.setText(_translate("addCV", "Submit"))
        self.plainTextEdit.setPlaceholderText(_translate("addCV", "Paste Your resume here!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addCV = QtWidgets.QMainWindow()
    ui = Ui_addCV()
    ui.setupUi(addCV)
    addCV.show()
    sys.exit(app.exec_())
