from PyQt5.QtWidgets import QWidget

from ui.ui_remain_ticket_widget import Ui_remainTicketWidget


class RemindTicketWidget(QWidget):
    def __init__(self, parent = None):
        super(RemindTicketWidget, self).__init__(parent)
        self.ui = Ui_remainTicketWidget()
        self.ui.setupUi(self)