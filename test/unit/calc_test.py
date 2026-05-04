import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator
from app.calc import InvalidPermissions

def mocked_validation(*args, **kwargs):
    return True

def mocked_incorrect_validation(*args, **kwargs):
    return False


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(6, 2))
        self.assertEqual(1, self.calc.substract(2, 1))
        self.assertEqual(5, self.calc.substract(10, 5))

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(16, self.calc.power(4, 2))
        self.assertEqual(125, self.calc.power(5, 3))

    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(2.0, self.calc.sqrt(4))
        self.assertEqual(5.0, self.calc.sqrt(25))
        self.assertEqual(4.0, self.calc.sqrt(16))

    def test_log_method_returns_correct_result(self):
        self.assertEqual(0.30102999566398114, self.calc.log(2))
        self.assertEqual(0.6989700043360187, self.calc.log(5))
        self.assertEqual(1.0, self.calc.log(10))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_fails_with_nan_parameter(self, _validate_permissions):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")

    @patch('app.util.validate_permissions', side_effect=mocked_incorrect_validation, create=True)
    def test_multiply_method_fails_with_invalid_permissions(self, _validate_permissions):
        self.assertRaises(InvalidPermissions, self.calc.multiply, 2, 2)

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")

    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "2")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())
    
    def test_sqrt_method_fails_with_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, -1)
        self.assertRaises(TypeError, self.calc.sqrt, -5)
        self.assertRaises(TypeError, self.calc.sqrt, -3)

    def test_log_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log, "2")
        self.assertRaises(TypeError, self.calc.log, None)
        self.assertRaises(TypeError, self.calc.log, object())

    def test_log_method_fails_with_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.log, -1)
        self.assertRaises(TypeError, self.calc.log, -5)
        self.assertRaises(TypeError, self.calc.log, -3)

    def test_log_method_fails_with_zero_parameter(self):
        self.assertRaises(TypeError, self.calc.log, 0)
    

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
