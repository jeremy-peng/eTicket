from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate, Qt

from ui.ui_buy_ticket_widget import Ui_BuyTicketWidget


class BuyTicketWidget(QWidget):
    hasTicketText = QTextCharFormat()
    hasTicketText.setForeground(Qt.black)
    hasTicketText.setBackground(Qt.green)


    def __init__(self, parent = None):
        super(BuyTicketWidget, self).__init__(parent)
        self.ui = Ui_BuyTicketWidget()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self):
        self.ui.btnSelectAllDays.clicked.connect(self.onSelectedAllDays)
        self.ui.btnInvertSelectedDays.clicked.connect(self.onInvertSelectedDays)
        self.ui.btnSelectAllWeekDays.clicked.connect(self.onSelectedAllWeekDays)
        self.ui.btnSelectAllWorkDays.clicked.connect(self.onSelectedAllWorkDays)


    def onSelectedAllDays(self):
        pass

    def onInvertSelectedDays(self):
        pass

    def onSelectedAllWorkDays(self):
        pass

    def onSelectedAllWeekDays(self):
        pass