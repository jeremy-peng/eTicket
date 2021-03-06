import unittest
from gui.BuyTicketDateModel import BuyTicketDateModel
from PyQt5.QtCore import QDate


class TestBusTicketDateModel(unittest.TestCase):
    def testInit(self):
        model = BuyTicketDateModel()
        model.setDate(2017, 12)
        self.assertEqual(len(model.getSelectedDays()), 0)
        model.selectAllDays()
        self.assertEqual(len(model.getSelectedDays()), 31)
        model.invertSelectDay()
        self.assertEqual(len(model.getSelectedDays()), 0)
        model.selectAllWeekDays()
        self.assertEqual(len(model.getSelectedDays()), 10)
        model.invertSelectDay()
        self.assertEqual(len(model.getSelectedDays()), 21)
        model.clearSelectedDays()
        model.selectAllWorkDays()
        self.assertEqual(len(model.getSelectedDays()), 21)
        self.assertFalse(model.hasSelectedDate(QDate(2017, 12, 3)))
        model.removeSelectedDate(QDate(2017, 12, 3))
        self.assertEqual(len(model.getSelectedDays()), 21)
        self.assertTrue(model.hasSelectedDate(QDate(2017, 12, 4)))
        model.removeSelectedDate(QDate(2017, 12, 4))
        self.assertFalse(model.hasSelectedDate(QDate(2017, 12, 4)))
        self.assertEqual(len(model.getSelectedDays()), 20)
        self.assertEqual(len(model.getBookedDays()), 0)
        model.addBookedDate(QDate(2017, 12, 5))
        self.assertEqual(len(model.getSelectedDays()), 19)
        self.assertEqual(len(model.getBookedDays()), 1)

        model.addBookedDateList([QDate(2017, 12, 6), QDate(2017, 12, 7)])
        self.assertEqual(len(model.getSelectedDays()), 17)
        self.assertEqual(len(model.getBookedDays()), 3)
        self.assertTrue(model.hasBookedDate(QDate(2017, 12, 5)))
        self.assertTrue(model.hasBookedDate(QDate(2017, 12, 6)))
        self.assertTrue(model.hasBookedDate(QDate(2017, 12, 7)))
        self.assertFalse(model.hasBookedDate(QDate(2017, 12, 8)))
        model.addBookedDate(QDate(2017, 12, 5))
        self.assertEqual(len(model.getBookedDays()), 3)

        model.setBookedDate([QDate(2017, 12, 8), QDate(2017, 12, 9)])
        self.assertEqual(len(model.getBookedDays()), 2)

        model.setDate(2017, 11)
        self.assertEqual(len(model.getSelectedDays()), 0)
        model.selectAllDays()
        self.assertEqual(len(model.getSelectedDays()), 30)
        model.invertSelectDay()
        self.assertEqual(len(model.getSelectedDays()), 0)
        model.selectAllWeekDays()
        self.assertEqual(len(model.getSelectedDays()), 8)
        model.invertSelectDay()
        self.assertEqual(len(model.getSelectedDays()), 22)
        model.clearSelectedDays()
        model.selectAllWorkDays()
        self.assertEqual(len(model.getSelectedDays()), 22)
        self.assertFalse(model.hasSelectedDate(QDate(2017, 12, 3)))
        model.removeSelectedDate(QDate(2017, 12, 3))
        self.assertEqual(len(model.getSelectedDays()), 22)
        self.assertTrue(model.hasSelectedDate(QDate(2017, 11, 6)))
        model.removeSelectedDate(QDate(2017, 11, 6))
        self.assertFalse(model.hasSelectedDate(QDate(2017, 11, 6)))
        self.assertEqual(len(model.getSelectedDays()), 21)


if __name__ == '__main__':
    unittest.main()
