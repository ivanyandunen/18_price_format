import unittest
from format_price import format_price


class Format_Price_Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(format_price(0.10), '0.10')

    def test2(self):
        self.assertEqual(format_price('12345,6789'), None)

    def test3(self):
        self.assertEqual(format_price(-76543.21), '-76 543.21')

    def test4(self):
        self.assertEqual(format_price(' '), None)

    def test5(self):
        self.assertEqual(format_price('-'), None)

    def test6(self):
        self.assertEqual(format_price(0.), '0.00')

    def test7(self):
        self.assertEqual(format_price(.567), '0.57')

    def test8(self):
        self.assertEqual(format_price('string'), None)

    def test9(self):
        self.assertEqual(format_price('23 657'), None)

    def test10(self):
        self.assertEqual(format_price(12345.6789), '12 345.68')


if __name__ == '__main__':
    unittest.main()
