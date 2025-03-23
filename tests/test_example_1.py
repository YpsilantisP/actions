# using unitest lib

import unittest


class TestExample(unittest.TestCase):
    def test(self):
        self.assertEqual(1, 1)

    def test_1(self):
        self.assertTrue(2 == 2)


if __name__ == '__main__':
    unittest.main()
