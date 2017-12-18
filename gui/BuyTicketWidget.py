from PyQt5.QtWidgets import QWidget

from ui.ui_buy_ticket_widget import Ui_BuyTicketWidget


class BuyTicketWidget(QWidget):
    def __init__(self, parent = None):
        super(BuyTicketWidget, self).__init__(parent)
        self.ui = Ui_BuyTicketWidget()
        self.ui.setupUi(self)