import unittest
from format_price import format_price


class FormatPriceTest(unittest.TestCase):
    def integer_part_is_zero(self):
        self.assertEqual(format_price(0.10), '0.10')

    def decimal_part_is_zero(self):
        self.assertEqual(format_price(3245.000000), '3 245')

    def input_is_int(self):
        self.assertEqual(format_price(12345), '12 345')

    def input_is_float(self):
        self.assertEqual(format_price(12345.6789), '12 345.68')

    def input_is_minus(self):
        self.assertEqual(format_price(-76543.21), '-76 543.21')

    def input_is_empty(self):
        self.assertIsNone(format_price(' '))

    def input_without_decimal_part(self):
        self.assertEqual(format_price(0.), '0')

    def input_without_integer_part(self):
        self.assertEqual(format_price(.567), '0.57')

    def input_is_string(self):
        self.assertIsNone(format_price('string'))


if __name__ == '__main__':
    unittest.main()
