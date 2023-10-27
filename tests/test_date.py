import unittest
import datetime
import jdatetime
from tarix.date import Date


class TestDate(unittest.TestCase):

    def setUp(self) -> None:
        self.date = Date('1402-08-08')

    def test_has_attr(self):
        self.assertTrue(hasattr(self.date, "date_str"))

    def test_from_str(self):
        self.assertIsInstance(self.date.from_str(), jdatetime.date)

    def test_jalali_to_gregorian(self):
        self.assertIsInstance(self.date.jalali_to_gregorian(), datetime.date)


if __name__ == "__main__":
    unittest.main()
