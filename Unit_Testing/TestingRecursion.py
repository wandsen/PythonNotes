from UnitTest_example import *
import unittest

class TestMyFunction (unittest.TestCase):
    def test_contains_simple_true(self):
        self.assertTrue(addition)
        self.assertTrue(recursion_factorial(8))

    def test_addition_equal(self):
        self.assertEqual(addition(), 10)

    def test_contains_simple_false(self):
        self.assertFalse(recursion_factorial(-8))

if __name__ == '__main__':
    unittest.main(exit=False) #if test fails, it might go into endless loop, this statement is to prevent that