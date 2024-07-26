import unittest
from function_zero import *
from functools import partial

class MyTestCase(unittest.TestCase):

    def test_change_types(self):
        self.assertEqual(ChangeType.turn_to_list(123), [1, 2, 3])
        self.assertEqual(ChangeType.turn_to_list("word"), ["w", "o", "r", "d"])
        self.assertEqual(ChangeType.turn_to_string(123), "123")
        self.assertEqual(ChangeType.turn_to_string(i for i in range(4)), "0123")
        self.assertEqual(ChangeType.turn_to_int([1, 2, 3]), 123)
        self.assertRaises(ChangeType.turn_to_int("a"), ValueError)


if __name__ == '__main__':
    unittest.main()
