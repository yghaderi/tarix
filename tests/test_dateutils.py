import unittest
from tarix.dateutils import dateutils


class TestDate(unittest.TestCase):

    def setUp(self) -> None:
        self.end = "1402-08-06"
        self.start = "1402-05-25"

    def test_days(self):
        self.assertIsInstance(dateutils.days(end=self.end, start=self.start), int)
        self.assertEqual(dateutils.days(end=self.end, start=self.start), 73)
        self.assertEqual(dateutils.days(end=self.start, start=self.end), -73)
        self.assertLess(dateutils.days(end=self.start), 0)

    def test_evenly_periods(self):
        self.assertEqual(dateutils.evenly_periods(length=3, end=self.end,start=self.start), (0, 0.8111111111111111))
        self.assertEqual(dateutils.evenly_periods(length=3, end='1401-05-25',start="1402-08-06"), (4, 0.8111111111111111))


if __name__ == "__main__":
    unittest.main()
