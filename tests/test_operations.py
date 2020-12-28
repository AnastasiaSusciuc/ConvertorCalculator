"""

Susciuc Anastasia

"""
import unittest

from operations.algorithms import Conversions, Operations
from service.service import Service


class TestOperations(unittest.TestCase):

    def test_addition(self):
        operation = Operations()
        conversions = Conversions()
        service = Service(operation, conversions)

        result = service.add("2", "1001001", "1001101110")
        self.assertEqual(result, "1010110111")

        result = service.add("3", "1002102", "1001")
        self.assertEqual(result, "1010110")

        result = service.add("10", "1891083792", "983729")
        self.assertEqual(result, "1892067521")

        result = service.add("16", "1ABDEF3792", "9AF9")
        self.assertEqual(result, "1ABDEFD28B")

        result = service.add("8", "65261", "0")
        self.assertEqual(result, "65261")

        result = service.add("8", "65", "66")
        self.assertEqual(result, "153")

        with self.assertRaises(ValueError) as cm:
            service.add("13", "1891083792", "983729")
        err = cm.exception
        self.assertEqual(str(err), "Invalid base")

        with self.assertRaises(ValueError) as cm:
            service.add("7", "1891083792", "983729")
        err = cm.exception
        self.assertEqual(str(err), "All digits must be smaller than the base!")

        with self.assertRaises(ValueError) as cm:
            service.add("7", "-5161", "5")
        err = cm.exception
        self.assertEqual(str(err), "Invalid input!")

    def test_subtraction(self):
        operation = Operations()
        conversions = Conversions()
        service = Service(operation, conversions)

        result = service.subtract("2", "1001001", "1010")
        self.assertEqual(result, "111111")

        result = service.subtract("8", "726516", "55552")
        self.assertEqual(result, "650744")

        result = service.subtract("10", "9999999", "0")
        self.assertEqual(result, "9999999")

        result = service.subtract("16", "9999999", "0")
        self.assertEqual(result, "9999999")

        result = service.subtract("16", "ABE45", "865F")
        self.assertEqual(result, "A37E6")

        result = service.subtract("5", "120421", "1111")
        self.assertEqual(result, "114310")

        with self.assertRaises(ValueError) as cm:
            service.subtract("13", "1891083792", "983729")
        err = cm.exception
        self.assertEqual(str(err), "Invalid base")

        with self.assertRaises(ValueError) as cm:
            service.subtract("7", "1891083792", "983729")
        err = cm.exception
        self.assertEqual(str(err), "All digits must be smaller than the base!")

        with self.assertRaises(ValueError) as cm:
            service.subtract("7", "-5161", "5")
        err = cm.exception
        self.assertEqual(str(err), "Invalid input!")

        with self.assertRaises(ValueError) as cm:
            service.subtract("7", "625", "112236")
        err = cm.exception
        self.assertEqual(str(err), "Cannot subtract numbers, the second is greater than the first!")

    def test_multiplication(self):
        operation = Operations()
        conversions = Conversions()
        service = Service(operation, conversions)

        result = service.multiply("2", "1001001", "0")
        self.assertEqual(result, "0")

        result = service.multiply("2", "1001001", "1")
        self.assertEqual(result, "1001001")

        result = service.multiply("5", "1003241", "4")
        self.assertEqual(result, "4024114")

        result = service.multiply("7", "652625610", "6")
        self.assertEqual(result, "5543330160")

        result = service.multiply("10", "8700912947", "6")
        self.assertEqual(result, "52205477682")

        result = service.multiply("16", "AB5672FE", "A")
        self.assertEqual(result, "6B1607DEC")

        with self.assertRaises(ValueError) as cm:
            service.multiply("7", "-5161", "5")
        err = cm.exception
        self.assertEqual(str(err), "Invalid input!")

        with self.assertRaises(ValueError) as cm:
            service.multiply("18", "5161", "5")
        err = cm.exception
        self.assertEqual(str(err), "Invalid base")

        with self.assertRaises(ValueError) as cm:
            service.multiply("8", "5161", "57")
        err = cm.exception
        self.assertEqual(str(err), "second number should be a single digit number")

        with self.assertRaises(ValueError) as cm:
            service.multiply("8", "5161", "J")
        err = cm.exception
        self.assertEqual(str(err), "second number is invalid!")

    def test_division(self):
        operation = Operations()
        conversions = Conversions()
        service = Service(operation, conversions)

        result, rem = service.divide("2", "1001001", "1")
        self.assertEqual(result, "1001001")
        self.assertEqual(rem, "0")

        result, rem = service.divide("7", "652651", "5")
        self.assertEqual(result, "123251")
        self.assertEqual(rem, "3")

        result, rem = service.divide("10", "98153", "6")
        self.assertEqual(result, "16358")
        self.assertEqual(rem, "5")

        result, rem = service.divide("16", "98A1F5C3", "7")
        self.assertEqual(result, "15CDFE89")
        self.assertEqual(rem, "4")

        with self.assertRaises(ValueError) as cm:
            service.divide("7", "-5161", "5")
        err = cm.exception
        self.assertEqual(str(err), "Invalid input!")

        with self.assertRaises(ValueError) as cm:
            service.divide("18", "5161", "5")
        err = cm.exception
        self.assertEqual(str(err), "Invalid base!")

        with self.assertRaises(ValueError) as cm:
            service.divide("8", "5161", "57")
        err = cm.exception
        self.assertEqual(str(err), "second number should be a single digit number!")

        with self.assertRaises(ValueError) as cm:
            service.divide("8", "5161", "H")
        err = cm.exception
        self.assertEqual(str(err), "second number is invalid!")

        with self.assertRaises(ValueError) as cm:
            service.divide("8", "5161", "0")
        err = cm.exception
        self.assertEqual(str(err), "can't divide by zero!")


if __name__ == '__main__':
    unittest.main()
