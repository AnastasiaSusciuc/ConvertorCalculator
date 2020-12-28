"""

Susciuc Anastasia

"""

class Service:

    def __init__(self, algorithms, conversions):
        self.__digit_to_char = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
                                10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        self.__char_to_digit = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                                "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "10": 10, "16": 16}
        self.__calculator = algorithms
        self.__converter = conversions

    def digit_list_to_string(self, digits):
        """
        transforms a list of digits into a string
        it eliminates all the irrelevant zeros
        :param digits: a list of digits
        :return: string
        """
        result = ""

        while len(digits) > 1 and digits[-1] == 0:
            digits.pop()

        digits.reverse()
        for i in range(0, len(digits)):
            result = result + self.__digit_to_char[digits[i]]
        return result

    def transform_string_to_list_of_digits(self, number, base, length):
        """
        transforms a string into a list of digits
        :param number:   string
        :param base:     int
        :param length:   the length of 'number'
        :return: a list of digits that taken in reverse order form the number 'number'
        :raises ValueError if the number's digits are greater than 'base'
                           if not all the characters in the string are valid digits
        """
        if len(number) < length:
            number = (length - len(number)) * "0" + number

        digits = []

        for i in reversed(range(0, length)):  # range(length - 1, -1, -1):
            digit = number[i]

            if digit not in self.__char_to_digit:
                raise ValueError("Invalid input!")

            digit = self.__char_to_digit[digit]

            if digit >= base:
                raise ValueError("All digits must be smaller than the base!")

            digits.append(digit)

        return digits

    def add(self, base, num1, num2):
        """
        the service for addition of two positive numbers in the same base
        transforms 'base' in int
        transforms 'num1' and 'num2' in a lists of digits
        :param base:       string
        :param num1:       string
        :param num2:       string
        :return:           a string represented the result of the subtraction
        raises ValueError  if the base is not from {2, 3, .., 10, 16}
        """
        len1 = len(num1)
        len2 = len(num2)
        length = max(len1, len2)

        if base not in self.__char_to_digit:
            raise ValueError("Invalid base")
        base = self.__char_to_digit[base]

        number1 = self.transform_string_to_list_of_digits(num1, base, length)
        number2 = self.transform_string_to_list_of_digits(num2, base, length)

        result_in_digits = self.__calculator.add(base, number1, number2)
        return self.digit_list_to_string(result_in_digits)

    def subtract(self, base, num1, num2):
        """
        the service for subtraction of two positive numbers in the same base
        transforms 'base' in int
        transforms 'num1' and 'num2' in a lists of digits
        :param base:       string
        :param num1:       string
        :param num2:       string
        :return:           a string represented the result of the subtraction
        raises ValueError  if the base is not from {2, 3, .., 10, 16}
        """
        len1 = len(num1)
        len2 = len(num2)
        length = max(len1, len2)

        if base not in self.__char_to_digit:
            raise ValueError("Invalid base")
        base = self.__char_to_digit[base]

        number1 = self.transform_string_to_list_of_digits(num1, base, length)
        number2 = self.transform_string_to_list_of_digits(num2, base, length)

        result_in_digits = self.__calculator.subtract(base, number1, number2, length)
        return self.digit_list_to_string(result_in_digits)

    def multiply(self, base, num1, num2):
        """
        the service for multiplication of two positive numbers in the same base
        transforms 'base' in int
        transforms 'num1' and 'num2' in a lists of digits
        :param base:     string
        :param num1:     string
        :param num2:     string
        :return:         a string represented the result of the multiplication
        raises ValueError if the second number is not a single digit valid number
                          if the base is not from {2, 3, .., 10, 16}
        """
        len1 = len(num1)
        len2 = len(num2)
        if len2 != 1:
            raise ValueError("second number should be a single digit number")
        if base not in self.__char_to_digit:
            raise ValueError("Invalid base")
        base = self.__char_to_digit[base]
        number1 = self.transform_string_to_list_of_digits(num1, base, len1)
        if num2 not in self.__char_to_digit:
            raise ValueError("second number is invalid!")
        number2 = self.__char_to_digit[num2]

        result_in_digits = self.__calculator.multiply(base, number1, number2, len1)
        return self.digit_list_to_string(result_in_digits)

    def divide(self, base, num1, num2):
        """
        the service for division of two positive numbers in the same base
        transforms 'base' in int
        transforms 'num1' and 'num2' in a lists of digits
        :param base:     string
        :param num1:     string
        :param num2:     string
        :return:         a string represented the quotient of the division and the remainder
        raises ValueError if the second number is not a single digit valid number
                          if the base is not from {2, 3, .., 10, 16}
                          if num2 is zero
        """
        len1 = len(num1)
        len2 = len(num2)
        if len2 != 1:
            raise ValueError("second number should be a single digit number!")

        if base not in self.__char_to_digit:
            raise ValueError("Invalid base!")
        base = self.__char_to_digit[base]

        number1 = self.transform_string_to_list_of_digits(num1, base, len1)

        if num2 not in self.__char_to_digit:
            raise ValueError("second number is invalid!")

        number2 = self.__char_to_digit[num2]

        if number2 == 0:
            raise ValueError("can't divide by zero!")

        result_in_digits, remainder = self.__calculator.divide(base, number1, number2, len1)
        result_in_digits.reverse()
        return self.digit_list_to_string(result_in_digits), self.__digit_to_char[remainder]

    def substitution(self, base1, num, base2):
        """
        the service for conversions using substitution method
        transforms 'base1', 'base2' in ints
        transforms 'number' in a list of digits
        :param base1:    string
        :param num:      string
        :param base2:    string
        :return:         a string represented the converted number
        raises ValueError if base1 or base2 are not valid
                          if base2 is less than base1
        """
        if base1 not in self.__char_to_digit:
            raise ValueError("First base is invalid!")
        base1 = self.__char_to_digit[base1]

        if base2 not in self.__char_to_digit:
            raise ValueError("Second base is invalid!")
        base2 = self.__char_to_digit[base2]

        if base2 < base1:
            raise ValueError("The base to convert the number should be smaller than the initial base!")

        number = self.transform_string_to_list_of_digits(num, base1, len(num))

        result = self.__converter.substitution(base1, base2, number)
        return self.digit_list_to_string(result)

    def divisions(self, base1, num, base2):
        """
       the service for conversions using successive divisions
       transforms 'base1', 'base2' in ints
       transforms 'number' in a list of digits
       :param base1:    string
       :param num:      string
       :param base2:    string
       :return:         a string represented the converted number
       raises ValueError if base1 or base2 are not valid
                         if base2 is greater than base1
       """
        if base1 not in self.__char_to_digit:
            raise ValueError("First base is invalid!")
        base1 = self.__char_to_digit[base1]

        if base2 not in self.__char_to_digit:
            raise ValueError("Second base is invalid!")
        base2 = self.__char_to_digit[base2]

        if base2 > base1:
            raise ValueError("The base to convert the number should be greater than the initial base!")

        number = self.transform_string_to_list_of_digits(num, base1, len(num))

        result = self.__converter.successive_divisions(base1, base2, number)
        return self.digit_list_to_string(result)

    def rapid(self, base1, num, base2):
        """
        the service for conversions using rapid conversions
        transforms 'base1', 'base2' in ints
        transforms 'number' in a list of digits
        :param base1:   string
        :param num:  string
        :param base2:   string
        :return:        a string represented the converted number
        raises ValueError if base1 or base2 are not valid
                          if base1 or base2 are not from [2, 4, 8, 16]
        """
        if base1 not in self.__char_to_digit:
            raise ValueError("First base is invalid!")
        base1 = self.__char_to_digit[base1]

        if base2 not in self.__char_to_digit:
            raise ValueError("Second base is invalid!")
        base2 = self.__char_to_digit[base2]

        if base1 not in [2, 4, 8, 16]:
            raise ValueError("The base should be a valid power of 2")
        if base2 not in [2, 4, 8, 16]:
            raise ValueError("The base should be a valid power of 2")

        number = self.transform_string_to_list_of_digits(num, base1, len(num))
        result = self.__converter.rapid_conversions(base1, base2, number)
        return self.digit_list_to_string(result)

    def intermediate(self, base1, number, base2):
        """
        the service for conversions using 10 as intermediate base
        transforms 'base1', 'base2' in ints
        transforms 'number' in a list of digits
        :param base1:   string
        :param number:  string
        :param base2:   string
        :return:        a string represented the converted number
        raises ValueError if base1 or base2 are not valid
        """
        if base1 not in self.__char_to_digit:
            raise ValueError("First base is invalid!")
        base1 = self.__char_to_digit[base1]

        if base2 not in self.__char_to_digit:
            raise ValueError("Second base is invalid!")
        base2 = self.__char_to_digit[base2]
        number = self.transform_string_to_list_of_digits(number, base1, len(number))
        result = self.__converter.intermediate_base_10(base1, base2, number)
        return self.digit_list_to_string(result)