from PyQt5 import QtCore, QtGui, QtWidgets
from Grons import Grons


class Ui_FormExit(object):
    def setupUi(self, Form):
        Form.setObjectName("FormExit")
        Form.resize(300, 200)
        self.pushButtonGoToMainWindow = QtWidgets.QPushButton(Form)
        self.pushButtonGoToMainWindow.setGeometry(QtCore.QRect(100, 50, 100, 22))
        self.pushButtonGoToMainWindow.setObjectName("pushButtonGoToMainWindow")
        self.labelText = QtWidgets.QLabel(Form)
        self.labelText.setGeometry(QtCore.QRect(70, 20, 200, 22))
        self.labelText.setObjectName("labelText")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Экран выхода"))
        self.labelText.setText(_translate("FormExit", "Перейти на главную страницу?"))
        self.pushButtonGoToMainWindow.setText(_translate("Form", "Главный экран"))

        # Adding my functions for UI.
        self.addFunctions()

    def addFunctions(self):
        self.pushButtonGoToMainWindow.clicked.connect(lambda: self.GoToMainWindow())

    # My functions.
    def GoToMainWindow(self):
        FormExit.close()
        print("The user is logout.")
        MainWindow.show()

# Личный кабинет
class Ui_FormPersonalAccount(object):
    def setupUi(self, Form):
        Form.setObjectName("FormPersonalAccount")
        Form.resize(600, 400)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 342, 222))
        self.textEdit.setObjectName("textEdit")
        self.lineEditFilePath = QtWidgets.QLineEdit(Form)
        self.lineEditFilePath.setGeometry(QtCore.QRect(20, 20, 342, 40))
        self.lineEditFilePath.setObjectName("lineEditFilePath")
        self.pushButtonDecode = QtWidgets.QPushButton(Form)
        self.pushButtonDecode.setGeometry(QtCore.QRect(380, 80, 142, 42))
        self.pushButtonDecode.setObjectName("pushButtonDecode")
        self.pushButtonEncode = QtWidgets.QPushButton(Form)
        self.pushButtonEncode.setGeometry(QtCore.QRect(380, 140, 142, 42))
        self.pushButtonEncode.setObjectName("pushButtonEncode")
        self.pushButtonExit = QtWidgets.QPushButton(Form)
        self.pushButtonExit.setGeometry(QtCore.QRect(380, 20, 142, 42))
        self.pushButtonExit.setObjectName("pushButtonExit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # My classes.
        self.grons = Grons('1132')
        # Adding my functions for UI.
        self.addFunctions()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Личный кабинет"))
        self.lineEditFilePath.setText(_translate("Form", "grons.txt"))
        self.pushButtonDecode.setText(_translate("Form", "Decode"))
        self.pushButtonEncode.setText(_translate("Form", "Encode"))
        self.pushButtonExit.setText(_translate("Form", "Exit"))

    def addFunctions(self):
        self.pushButtonEncode.clicked.connect(lambda: self.writeToEncodedFile(self.textEdit.toPlainText(), self.lineEditFilePath.text()))
        self.pushButtonDecode.clicked.connect(lambda: self.getTextFromEncodedFile(self.lineEditFilePath.text()))
        self.pushButtonExit.clicked.connect(lambda: self.Exit())

    # My functions.
    def Exit(self):
        FormPersonalAccount.close()
        FormExit.show()

    def gronsEncode(self, text: str):
        result = self.grons.encode(text)
        return result

    def gronsDecode(self, text: str):
        result = self.grons.decode(text)
        return result

    def writeToEncodedFile(self, text: str, filePath: str):
        with open(filePath, 'w') as file:
            file.write(self.gronsEncode(text))
        file.close()

    def getTextFromEncodedFile(self, filePath: str):
        self.textEdit.setText("")
        import os.path
        if os.path.exists(filePath):
            with open(filePath, 'r') as file:
                for line in file:
                    self.textEdit.setText(self.textEdit.toPlainText() + self.gronsDecode(line))

# Главная страница
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelUserName = QtWidgets.QLabel(self.centralwidget)
        self.labelUserName.setGeometry(QtCore.QRect(60, 30, 61, 21))
        self.labelUserName.setObjectName("labelUserName")
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setGeometry(QtCore.QRect(60, 70, 61, 21))
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditUserName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditUserName.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonSighInOrRegister = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSighInOrRegister.setGeometry(QtCore.QRect(60, 110, 181, 23))
        self.pushButtonSighInOrRegister.setObjectName("pushButtonSighIn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # My classes.
        self.grons = Grons('1132')
        # Adding my functions for UI.
        self.addFunctions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главная страница"))
        self.labelUserName.setText(_translate("MainWindow", "UserName: "))
        self.labelPassword.setText(_translate("MainWindow", "Password: "))
        self.pushButtonSighInOrRegister.setText(_translate("MainWindow", "SignIn / Register"))

    def addFunctions(self):
        self.pushButtonSighInOrRegister.clicked.connect(lambda: self.checkAccount(self.lineEditUserName.text(), self.lineEditPassword.text()))

    # My functions.
    def checkDataForSpecialCharacters(self, username, password):
        if (':' in username) or (':' in password):
            print("Error! Expected ':'.")
            return True;

    def gronsEncode(self, text: str):
        result = self.grons.encode(text)
        return result

    def gronsDecode(self, text: str):
        result = self.grons.decode(text)
        return result

    def checkAccount(self, username: str, password: str):
        if self.checkDataForSpecialCharacters(username, password) is True:
            return False
        gronsLine = str(self.gronsEncode(username)) + ":" + str(self.gronsEncode(password))
        with open('users.txt', 'r+') as file:
            if gronsLine in file.read():
                print("The user is logged in.")
                self.Login()
            else:
                file.write(gronsLine + '\n')
                print("The user is registered.")
                print("The user is logged in.")
                self.Login()

    def Login(self):
        MainWindow.close()
        FormPersonalAccount.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    FormPersonalAccount = QtWidgets.QWidget()
    ui = Ui_FormPersonalAccount()
    ui.setupUi(FormPersonalAccount)

    FormExit = QtWidgets.QWidget()
    ui = Ui_FormExit()
    ui.setupUi(FormExit)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

