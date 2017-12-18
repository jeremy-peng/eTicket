import sys
from gui import  Application



def main():
    try:
        app = Application.App(sys.argv)
        app.login()
        sys.exit(app.exec_())
    except:
        print(sys.exc_info()[0])



if __name__ == "__main__":
    main()

