import unittest
from gui.BuyTicketDateModel import BuyTicketDateModel


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

if __name__ == '__main__':
    unittest.main()
