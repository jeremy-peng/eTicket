import sys
from config import  userData
from eBus import  request
from gui import  Application



def main():
    app = Application.App(sys.argv)
    if request.validateUserData(userData.loginName, userData.customerId, userData.keyCode):
        app.showMainWindow()
    else:
        app.showLoginDialog()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

