"""

Susciuc Anastasia

"""
import unittest

from operations.algorithms import Operations, Conversions
from service.service import Service


class TestConversions(unittest.TestCase):

    def test_substitution_method(self):
        operation = Operations()
        conversions = Conversions()
        service = Service(operation, conversions)
        num = service.substitution("5", "32410", "9")
        self.assertEqual(num, "3047")
        num = service.substitution("9", "71682817", "16")
        self.assertEqual(num, "20D3988")
        num = service.substitution("9", "82711", "9")
        self.assertEqual(num, "82711")

        with self.assertRaises(ValueError) as cm:
            service.substitution("9", "82711", "7")
        err = cm.exception
        self.assertEqual(str(err), "The base to convert the number should be smaller than the initial base!")

        with self.assertRaises(ValueError) as cm:
            service.substitution("9", "82711", "H")
        err = cm.exception
        self.assertEqual(str(err), "Second base is invalid!")

        with self.assertRaises(ValueError) as cm:
            service.substitution("J", "82711", "8")
        err = cm.exception
        self.assertEqual(str(err), "First base is invalid!")

    def test_division_method(self):
        operation = Operations()
        conversions = Conversions()
        service = Service(operation, conversions)
        num = service.divisions("9", "32410", "5")
        self.assertEqual(num, "1141344")

        num = service.divisions("16", "A677BF", "10")
        self.assertEqual(num, "10909631")

        num = service.divisions("4", "322110", "3")
        self.assertEqual(num, "12010020")

        with self.assertRaises(ValueError) as cm:
            service.divisions("6", "51511", "7")
        err = cm.exception
        self.assertEqual(str(err), "The base to convert the number should be greater than the initial base!")

        with self.assertRaises(ValueError) as cm:
            service.divisions("9", "82711", "H")
        err = cm.exception
        self.assertEqual(str(err), "Second base is invalid!")

        with self.assertRaises(ValueError) as cm:
            service.divisions("J", "82711", "8")
        err = cm.exception
        self.assertEqual(str(err), "First base is invalid!")

    def test_rapid_conversions(self):
        operation = Operations()
        conversions = Conversions()
        service = Service(operation, conversions)

        num = service.rapid("4", "32110", "2")
        self.assertEqual(num, "1110010100")

        num = service.rapid("16", "AF579E", "8")
        self.assertEqual(num, "53653636")

        num = service.rapid("8", "53653636", "16")
        self.assertEqual(num, "AF579E")

        num = service.rapid("2", "101100111001", "8")
        self.assertEqual(num, "5471")

        num = service.rapid("2", "111", "4")
        self.assertEqual(num, "13")

        with self.assertRaises(ValueError) as cm:
            service.rapid("J", "82711", "8")
        err = cm.exception
        self.assertEqual(str(err), "First base is invalid!")

        with self.assertRaises(ValueError) as cm:
            service.rapid("9", "82711", "H")
        err = cm.exception
        self.assertEqual(str(err), "Second base is invalid!")

        with self.assertRaises(ValueError) as cm:
            service.rapid("6", "82711", "8")
        err = cm.exception
        self.assertEqual(str(err), "The base should be a valid power of 2")

        with self.assertRaises(ValueError) as cm:
            service.rapid("4", "82711", "9")
        err = cm.exception
        self.assertEqual(str(err), "The base should be a valid power of 2")

    def test_intermediate_base_10(self):
        operation = Operations()
        conversions = Conversions()
        service = Service(operation, conversions)

        num = service.intermediate("4", "32110", "2")
        self.assertEqual(num, "1110010100")

        num = service.intermediate("16", "ABCDE", "10")
        self.assertEqual(num, "703710")

        num = service.intermediate("10", "9991728", "4")
        self.assertEqual(num, "212013120300")

        num = service.intermediate("4", "1210201", "4")
        self.assertEqual(num, "1210201")

        num = service.intermediate("5", "41310", "16")
        self.assertEqual(num, "A91")

        with self.assertRaises(ValueError) as cm:
            service.intermediate("J", "82711", "8")
        err = cm.exception
        self.assertEqual(str(err), "First base is invalid!")

        with self.assertRaises(ValueError) as cm:
            service.intermediate("9", "82711", "H")
        err = cm.exception
        self.assertEqual(str(err), "Second base is invalid!")


if __name__ == '__main__':
    unittest.main()
