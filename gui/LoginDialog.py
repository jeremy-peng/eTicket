from ui.ui_login_dialog import Ui_LoginDialog
from PyQt5.QtWidgets import QDialog

class LoginDialog(QDialog):

    def __init__(self):
        super(LoginDialog, self).__init__()
        self.initUI()


    def initUI(self):
        self.ui = Ui_LoginDialog()
        self.ui.setupUi(self)


    def getInput(self):
        return self.ui.textPhoneNum.text(), self.ui.textPhonePin.text()
