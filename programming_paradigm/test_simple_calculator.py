import unittest
from .simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Test Addition ---
    def test_addition_positive_numbers(self):
        """Test addition with two positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        """Test addition with two negative numbers."""
        self.assertEqual(self.calc.add(-1, -5), -6)

    def test_addition_mixed_numbers(self):
        """Test addition with a positive and a negative number."""
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, -2), 3)

    def test_addition_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(-3, 0), -3)

    def test_addition_floats(self):
        """Test addition with floating-point numbers."""
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3) # Use assertAlmostEqual for floats

    # --- Test Subtraction ---
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtract_mixed_numbers(self):
        """Test subtraction with mixed positive/negative numbers."""
        self.assertEqual(self.calc.subtract(5, -2), 7)
        self.assertEqual(self.calc.subtract(-5, 2), -7)

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(7, 0), 7)
        self.assertEqual(self.calc.subtract(0, 3), -3)

    def test_subtract_floats(self):
        """Test subtraction with floating-point numbers."""
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2)

    # --- Test Multiplication ---
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiply_mixed_numbers(self):
        """Test multiplication with mixed positive/negative numbers."""
        self.assertEqual(self.calc.multiply(-2, 6), -12)
        self.assertEqual(self.calc.multiply(7, -1), -7)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, -5), 0)

    def test_multiply_floats(self):
        """Test multiplication with floating-point numbers."""
        self.assertEqual(self.calc.multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25)

    # --- Test Division ---
    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_divide_mixed_numbers(self):
        """Test division with mixed positive/negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)

    def test_divide_by_one(self):
        """Test division by one."""
        self.assertEqual(self.calc.divide(7, 1), 7.0)

    def test_divide_zero_by_number(self):
        """Test division of zero by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)

    def test_divide_by_zero(self):
        """Test division by zero, which should return None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Even 0/0 is typically undefined, here it matches the function's contract of returning None.

    def test_divide_floats(self):
        """Test division with floating-point numbers."""
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)

if __name__ == '__main__':
    unittest.main()