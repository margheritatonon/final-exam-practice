from practice import ListCalculator
import unittest

class TestListCalculator(unittest.TestCase):
    def test_one(self):
        lists = ListCalculator([10, 20, 30], [5, 10, 15])
        result = lists.division()
        expected = 0.5
        self.assertEqual(result, expected)
    
    def test_two(self):
        lists = ListCalculator([0, 0, 2], [6, 2, 4])
        result = lists.division()
        expected = 6
        self.assertEqual(result, expected)

unittest.main(argv=[''], verbosity=2, exit=False)