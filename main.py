import sys
from gui import  Application



def main():
    app = Application.App(sys.argv)
    app.login()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

