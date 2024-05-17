
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 570)
        MainWindow.setStyleSheet("background-color:#00A6FB")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 40, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color:#051923;\n"
"color:rgb(155, 222, 255);\n"
"border:2px solid rgb(155, 222, 255);\n"
"border-radius:20px;\n"
"padding-bottom:4px\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 160, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"background-color:#051923;\n"
"color:rgb(155, 222, 255);\n"
"border:2px solid rgb(155, 222, 255);\n"
"border-radius:20px\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(340, 165, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setStyleSheet("QLineEdit{\n"
"background-color:#051923;\n"
"color:rgb(155, 222, 255);\n"
"border:2px solid rgb(155, 222, 255);\n"
"border-radius:12px;\n"
"padding-left:10px\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(155, 222, 255);\n"
"color:#051923;\n"
"border:2px solid #051923\n"
"}")
        self.lineEdit_username.setText("")
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 230, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"background-color:#051923;\n"
"color:rgb(155, 222, 255);\n"
"border:2px solid rgb(155, 222, 255);\n"
"border-radius:20px\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_passord = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_passord.setGeometry(QtCore.QRect(340, 235, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_passord.setFont(font)
        self.lineEdit_passord.setStyleSheet("QLineEdit{\n"
"background-color:#051923;\n"
"color:rgb(155, 222, 255);\n"
"border:2px solid rgb(155, 222, 255);\n"
"border-radius:12px;\n"
"padding-left:10px\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(155, 222, 255);\n"
"color:#051923;\n"
"border:2px solid #051923\n"
"}")
        self.lineEdit_passord.setText("")
        self.lineEdit_passord.setObjectName("lineEdit_passord")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(30, 30, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("QPushButton{\n"
"background-color:#051923;\n"
"color:rgb(155, 222, 255);\n"
"border:2px solid rgb(155, 222, 255);\n"
"border-radius:12px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color:rgb(155, 222, 255);\n"
"color:#051923;\n"
"border:2px solid #051923\n"
"}")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.pushButton_register_db = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_register_db.setGeometry(QtCore.QRect(360, 410, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_register_db.setFont(font)
        self.pushButton_register_db.setStyleSheet("QPushButton{\n"
"background-color:#051923;\n"
"color:rgb(155, 222, 255);\n"
"border:2px solid rgb(155, 222, 255);\n"
"border-radius:50%;\n"
"}\n"
"QPushButton::hover{\n"
"background-color:rgb(155, 222, 255);\n"
"color:#051923;\n"
"border:2px solid #051923\n"
"}")
        self.pushButton_register_db.setObjectName("pushButton_register_db")
        self.lineEdit_confirm_passord = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_confirm_passord.setGeometry(QtCore.QRect(340, 320, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_confirm_passord.setFont(font)
        self.lineEdit_confirm_passord.setStyleSheet("QLineEdit{\n"
"background-color:#051923;\n"
"color:rgb(155, 222, 255);\n"
"border:2px solid rgb(155, 222, 255);\n"
"border-radius:12px;\n"
"padding-left:10px\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(155, 222, 255);\n"
"color:#051923;\n"
"border:2px solid #051923\n"
"}")
        self.lineEdit_confirm_passord.setText("")
        self.lineEdit_confirm_passord.setObjectName("lineEdit_confirm_passord")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 300, 191, 80))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"background-color:#051923;\n"
"color:rgb(155, 222, 255);\n"
"border:2px solid rgb(155, 222, 255);\n"
"border-radius:20px\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sign Up"))
        self.label_2.setText(_translate("MainWindow", "Username : "))
        self.lineEdit_username.setPlaceholderText(_translate("MainWindow", "Username...."))
        self.label_3.setText(_translate("MainWindow", "Password : "))
        self.lineEdit_passord.setPlaceholderText(_translate("MainWindow", "Password...."))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.pushButton_register_db.setText(_translate("MainWindow", "Accept"))
        self.lineEdit_confirm_passord.setPlaceholderText(_translate("MainWindow", "Confirm Password...."))
        self.label_4.setText(_translate("MainWindow", "Confirm\n"
"Password : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
