# using unitest lib

import unittest



class TestExample(unittest.TestCase):

    def test_always_passes(self):
        self.assertEqual(1, 1)

    def test_another_always_passes(self):
        self.assertTrue(2 == 2)


if __name__ == '__main__':
    unittest.main()
