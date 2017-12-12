from PyQt5.QtWidgets import QApplication, QDialog
import sys

from gui.LoginDialog import LoginDialog
from config import  userData

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = LoginDialog()
    dialog.loginName = userData.loginName
    if (dialog.exec_() == QDialog.Accepted):
        loginName, pin = dialog.getInput()
        userData.loginName = loginName
        userData.sync()
        sys.exit()
    else:
        sys.exit()

    sys.exit(app.exec_())

