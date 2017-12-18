import sys
from gui import  Application
import  logging


def main():
    try:
        initLog()
        app = Application.App(sys.argv)
        app.login()
        sys.exit(app.exec_())
    except:
        print(sys.exc_info()[0])

def initLog():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


if __name__ == "__main__":
    main()

