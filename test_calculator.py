import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        test_cases = [
            (1, 2, 3),
            (0, 0, 0),
            (-1, 1, 0),
            (3.5, 2.5, 6.0),
            (1000000, 1000000, 2000000)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expected)

    def test_divide(self):
        test_cases = [
            (4, 2, 2),
            (0, 1, 0),
            (-4, 2, -2),
            (3.0, 1.5, 2.0),
            (100, 10, 10)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.divide(a, b), expected)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

    def test_is_prime_number(self):
        test_cases = [
            (2, True),
            (3, True),
            (4, False),
            (1, False),
            (0, False),
            (-1, False),
            (17, True),
            (18, False),
            (997, True)
        ]
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(self.calc.is_prime_number(n), expected)