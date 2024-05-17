from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        MainWindow.setStyleSheet("background-color:#00A6FB")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 20, 191, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color:#051923;\n"
"color:#9BDEFF;\n"
"border:2px solid #9BDEFF;\n"
"border-radius:20px\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 100, 600, 330))
        self.listWidget.setStyleSheet("QListWidget{\n"
"background-color:#051923;\n"
"color:#9BDEFF;\n"
"border:2px solid #9BDEFF;\n"
"border-radius:15px\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 460, 340, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background-color:#051923;\n"
"color:#9BDEFF;\n"
"border:2px solid #9BDEFF;\n"
"border-radius:12px;\n"
"padding-left:10px\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 540, 370, 90))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"background-color:None\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 450, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:#051923;\n"
"color:#9BDEFF;\n"
"border:2px solid #9BDEFF;\n"
"border-radius:50%\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 460, 110, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"background-color:#051923;\n"
"color:#9BDEFF;\n"
"border:2px solid #9BDEFF;\n"
"border-radius:20px\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Check"))
        self.label_2.setText(_translate("MainWindow", "Attention :  When you click\n"
"on your item that\n"
"value will appear here ."))
        self.pushButton.setText(_translate("MainWindow", "Done"))
        self.label_3.setText(_translate("MainWindow", "Work :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
