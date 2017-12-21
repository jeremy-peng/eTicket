import unittest
from gui.BuyTicketDateModel import BuyTicketDateModel
from PyQt5.QtCore import QDate


class TestBusTicketDateModel(unittest.TestCase):
    def testInit(self):
        model = BuyTicketDateModel()
        model.setDate(2017, 12)
        self.assertEqual(len(model.getSeletedDays()), 0)
        model.selectAllDays()
        self.assertEqual(len(model.getSeletedDays()), 31)
        model.invertSelectDay()
        self.assertEqual(len(model.getSeletedDays()), 0)
        model.selectAllWeekDays()
        self.assertEqual(len(model.getSeletedDays()), 10)
        model.invertSelectDay()
        self.assertEqual(len(model.getSeletedDays()), 21)
        model.clearSelectedDays()
        model.selectAllWorkDays()
        self.assertEqual(len(model.getSeletedDays()), 21)
        self.assertFalse(model.hasDate(QDate(2017,12,3)))
        model.removeDate(QDate(2017,12,3))
        self.assertEqual(len(model.getSeletedDays()), 21)
        self.assertTrue(model.hasDate(QDate(2017, 12, 4)))
        model.removeDate(QDate(2017,12,4))
        self.assertFalse(model.hasDate(QDate(2017, 12, 4)))
        self.assertEqual(len(model.getSeletedDays()), 20)

        model.setDate(2017, 11)
        self.assertEqual(len(model.getSeletedDays()), 0)
        model.selectAllDays()
        self.assertEqual(len(model.getSeletedDays()), 30)
        model.invertSelectDay()
        self.assertEqual(len(model.getSeletedDays()), 0)
        model.selectAllWeekDays()
        self.assertEqual(len(model.getSeletedDays()), 8)
        model.invertSelectDay()
        self.assertEqual(len(model.getSeletedDays()), 22)
        model.clearSelectedDays()
        model.selectAllWorkDays()
        self.assertEqual(len(model.getSeletedDays()), 22)
        self.assertFalse(model.hasDate(QDate(2017, 12, 3)))
        model.removeDate(QDate(2017,12,3))
        self.assertEqual(len(model.getSeletedDays()), 22)
        self.assertTrue(model.hasDate(QDate(2017, 11, 6)))
        model.removeDate(QDate(2017,11,6))
        self.assertFalse(model.hasDate(QDate(2017, 11, 6)))
        self.assertEqual(len(model.getSeletedDays()), 21)


if __name__ == '__main__':
    unittest.main()
