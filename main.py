from PyQt5.QtWidgets import QApplication, QDialog
import sys

from gui.LoginDialog import LoginDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = LoginDialog()
    if (dialog.exec() == QDialog.Accepted):
        print(dialog.getInput())


    sys.exit(app.exec_())

