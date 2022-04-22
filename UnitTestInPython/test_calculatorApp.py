import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp

## assertEqual used to ensure that the returned results are as expected.
class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")
        self.patcher1 = patch('calculatorApp.add', return_value=5)
        self.MockClass1 = self.patcher1.start()
        self.addCleanup(self.patcher1.stop)

    def test_user_input(self):
        self.assertEqual(check_user_input("8"), 8)
        self.assertEqual(check_user_input("8.0"), 8.0)
        self.assertEqual(check_user_input(
            ""), ValueError("Input can't be empty"))

    def test_AddPass(self):
        self.assertEqual(add(8, 5), 13)  
        self.assertEqual(calculate('1', 8, 5), 2)  
    
    def test_AddInvalid(self):
        self.assertNotEqual(calculate('1', 8, 5), 2)

    def test_substraction(self):
        self.assertEqual(subtract(8, 5), 3)
        self.assertEqual(calculate('2', 8, 5), 3)

    def test_multiplication(self):
        self.assertEqual(multiply(8, 5), 40)
        self.assertEqual(calculate('3', 8, 5), (8, '*', 5, '=', 40))

    def test_division(self):
        self.assertEqual(divide(8, 5), 1.6)
        self.assertEqual(divide(0, 8), 0)
        self.assertEqual(divide(8, 0), "You can't divide by zero!")

    def test_calculate_division(self):
        self.assertEqual(calculate('4', 0, 8), 0)
        self.assertEqual(calculate('4', 8, 5), (8, '/', 5, '=', 1.6))

    def test_calculate_devision_by_zero(self):
        self.assertEqual(calculate('4', 8, 0), 5)

    def test_divisionInvalid(self):
        self.assertNotEqual(divide(8, 5), 13)
        self.assertNotEqual(divide(0, 8), 5)
        self.assertNotEqual(divide(8, 0), 8)

    def test_calculate_invalidInput(self):
        self.assertEqual(calculate('4', "", 5), (8, '/', 5, '=', 1.6))

    def test_calculate_choice(self):
        self.assertEqual(calculate('5', 8, 5), 13)

    def test_Exist(self):
        self.assertEqual(isExit("yes"), False)
        self.assertEqual(isExit("no"), True)
        self.assertEqual(isExit(""), True)

    def test_DividByZerrorEx1(self):
        with self.assertRaises(ValueError):
            calculate('4', '3', 'D')

    # OR

    def test_DividByZerrorEx2(self):
        self.assertRaises(ValueError, calculate, '4', '3', 'D')

    def test_DividByZerrorRegex(self):
        with self.assertRaisesRegex(ValueError, "input is not a number!"):
            calculate('4', '3', 'D')

    def test_AddPassWithMockEx1(self):
        with mock.patch('calculatorApp.add', return_value=6):
            result = calculate('1', 2, 4)
        self.assertEqual(result, 6)

    @mock.patch('calculatorApp.add', return_value=4)
    def test_AddPassWithMockEx2(self, mock_check):
        result = calculate('1', 3, 2)
        self.assertEqual(result, 4)

    def test_AddPassWithMocEx3(self):
        assert calculatorApp.add is self.MockClass1
        self.assertEqual(calculate('1', 2, 6), 5)

    def tearDown(self):
        print("tearDown .. ")
        # self.patcher1.stop()#or add this and remove self.addCleanup(self.patcher1.stop) in startup but this is not recommened!


class TestCalculateWithoutMock(unittest.TestCase):
    def test_AddPass(self):
        self.assertEqual(add(6, 3), 9)
        self.assertEqual(calculate('1', 6, 3), 9)


if __name__ == '__main__':
    unittest.main()
