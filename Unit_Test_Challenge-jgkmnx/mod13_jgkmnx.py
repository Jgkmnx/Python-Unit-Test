import unittest
from datetime import datetime

def valid_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7


def valid_chart(choice):
    return choice in ('1', '2')


def valid_time(choice):
    return choice in ('1', '2', '3', '4')


def valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def valid_range(start, end):
    try:
        start_dt = datetime.strptime(start, "%Y-%m-%d")
        end_dt = datetime.strptime(end, "%Y-%m-%d")
        return end_dt >= start_dt
    except ValueError:
        return False
    


class input_unit_test(unittest.TestCase):

    def symbol_test(self):
        self.assertTrue(valid_symbol("GOOGL"))
        self.assertFalse(valid_symbol("GOOGL123"))
        self.assertFalse(valid_symbol(""))

    def chart_test(self):
        self.assertTrue(valid_chart("1"))
        self.assertTrue(valid_chart("2"))
        self.assertFalse(valid_chart("18"))
        self.assertFalse(valid_chart("0"))
        self.assertFalse(valid_chart("AAA"))

    def time_test(self):
        self.assertTrue(valid_time("1"))
        self.assertTrue(valid_time("4"))
        self.assertFalse(valid_time("20"))
        self.assertFalse(valid_time("AAA"))

    def date_test(self):
        self.assertTrue(valid_date("2004-12-25"))
        self.assertFalse(valid_date("12-20-2004"))
        self.assertFalse(valid_date("2004/02/20"))
        self.assertFalse(valid_date(""))

    def date_range_test(self):
        self.assertTrue(valid_range("2004-01-01", "2004-12-01"))
        self.assertTrue(valid_range("2004-02-20", "2004-02-20"))
        self.assertFalse(valid_range("2004-01-02", "2004-01-01"))

if __name__ == "__main__":
    unittest.main()