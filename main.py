import unittest

from test_calculator import TestCalculator

suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
result = unittest.TextTestRunner(verbosity=2).run(suite)
print(result)