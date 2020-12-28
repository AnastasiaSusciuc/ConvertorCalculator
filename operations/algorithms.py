"""

Susciuc Anastasia

"""

import math


class Operations:

    @staticmethod
    def add(base, num1, num2):
        """
        adding two numbers that are in base 'base'
        :param base: a number from {2, 3, .., 10, 16}
        :param num1: a list containing the digits of the given number in reverse order
        :param num2: a list containing the digits of the given number in reverse order
        :return: a list of digits that form the result of the addition num1+num2
        """

        result_digits = []

        length = max(len(num1), len(num2))

        for i in range(len(num1), length + 1):   # filling the first number with irrelevant zeros
            num1.append(0)

        for i in range(len(num2), length + 1):   # filling the second number with irrelevant zeros
            num2.append(0)

        carry = 0
        for i in range(0, length):
            digit10 = (num1[i] + num2[i] + carry) % base
            carry = (num1[i] + num2[i] + carry) // base
            result_digits.append(digit10)

        if carry != 0:                            # if the result has more digits than the greater one
            result_digits.append(carry)

        return result_digits

    @staticmethod
    def subtract(base, num1, num2, length):
        """
        :param base: a number from {2, 3, .., 10, 16}
        :param num1: a list containing the digits of the given number in reverse order
        :param num2: a list containing the digits of the given number in reverse order
        :param length: the length of the greatest number between num1 and num2
        :return: a list of digits that form the result of the subtraction num1-num2
        raises ValueError if the first number is smaller than the second one
        """
        result_digits = []
        borrow = 0
        for i in range(0, length):
            digit10 = num1[i]-num2[i]-borrow
            if digit10 < 0:
                digit10 = digit10 + base
                borrow = 1
            else:
                borrow = 0

            result_digits.append(digit10)

        if borrow != 0:                             # if there is still a non zero borrow the result is negative
            raise ValueError("Cannot subtract numbers, the second is greater than the first!")

        return result_digits

    @staticmethod
    def multiply(base, num1, num2, length):
        """
        multiplication by one digit
        :param base: a number from {2, 3, .., 10, 16}
        :param num1: a list containing the digits of the given number in reverse order
        :param num2: a single digit number
        :param length: the length of num1
        :return: a list of digits that form the result of the multiplication num1*num2
        """
        result_digits = []
        carry = 0
        for i in range(0, length):
            digit10 = num1[i]*num2 + carry
            carry = digit10 // base
            digit10 = digit10 % base
            result_digits.append(digit10)

        if carry != 0:
            result_digits.append(carry)

        return result_digits

    @staticmethod
    def divide(base, num1, num2, length):
        """
        division by one digit
        :param base: a number from {2, 3, .., 10, 16}
        :param num1: a list containing the digits of the given number in reverse order
        :param num2: a single digit number
        :param length: the length of num1
        :return: a list of digits that form the result of the division num1/num2 +
                                a number that represents the remainder
        """
        remainder = 0
        result_digits = []

        if num2 == 0:
            raise ValueError("Can't divide by zero!")

        for i in reversed(range(length)):
            digit10 = remainder*base + num1[i]
            result_digits.append(digit10 // num2)
            remainder = digit10 % num2

        return result_digits, remainder


class Conversions:

    @staticmethod
    def substitution(base1, base2, number):
        """
        the algorithm for the method of successive divisions
        base1 is smaller than base2
        :param base1: a number from {2, 3, .., 10, 16}
        :param base2: a number from {2, 3, .., 10, 16}
        :param number: a list containing the digits of the given number in reverse order
        :return: a list of digits that form in reverse order the number 'number' in base 'base2'
        """

        positional_pow = [1]
        result = [0]

        for i in range(0, len(number)):
            positional_value = Operations.multiply(base2, positional_pow, number[i], len(positional_pow))
            result = Operations.add(base2, result, positional_value)
            positional_pow = Operations.multiply(base2, positional_pow, base1, len(positional_pow))

        return result

    @staticmethod
    def is_zero(number):
        """
        checks if a list of digits is all zero
        :param number: a list of digits
        :return: True if all the digits from the list are 0
                 False otherwise
        """
        for i in number:
            if i != 0:
                return False
        return True

    @staticmethod
    def successive_divisions(base1, base2, number):
        """
        the algorithm for the substitution method
        base1 is greater than base2
        :param base1: a number from {2, 3, .., 10, 16}
        :param base2: a number from {2, 3, .., 10, 16}
        :param number: a list containing the digits of the given number in reverse order
        :return: a list of digits that form the number 'number' in base 'base2'
        """
        result = []

        while not Conversions.is_zero(number):
            number, remainder = Operations.divide(base1, number, base2, len(number))
            number.reverse()        # we need to reverse the number because the divide method returns it reversed
            result.append(remainder)

        return result

    @staticmethod
    def rapid_conversions(base1, base2, number):
        """
        the algorithm for rapid conversions
        :param base1: a number from {2, 3, .., 10, 16}
        :param base2: a number from {2, 3, .., 10, 16}
        :param number: a list containing the digits of the given number in reverse order
        :return:  a list of digits that form the number 'number' in base 'base2'
        """

        log1 = int(math.log2(base1))    # how many bits form a digit in base1
        log2 = int(math.log2(base2))    # how many bits form a digit in base2

        num_base_two = []               # we take every digit and transform it in log1 bits
        for digit in number:
            for _ in range(log1):
                num_base_two.append(digit % 2)
                digit //= 2

        while not len(num_base_two) % log2 == 0:  # filling with irrelevant zeros
            num_base_two.append(0)

        result = []
        for i in range(0, len(num_base_two), log2):  # we group every log2 bits to form a digit for the new number
            digit = 0
            for j in range(log2):
                digit = digit + (1 << j) * num_base_two[i+j]

            result.append(digit)

        return result

    @staticmethod
    def intermediate_base_10(base1, base2, number):
        """
        the algorithm that used 10 as an intermediate base
        :param base1: a number from {2, 3, .., 10, 16}
        :param base2: a number from {2, 3, .., 10, 16}
        :param number: a list containing the digits of the given number in reverse order
        :return:  a list of digits that form the number 'number' in base 'base2'
        """
        if base1 == base2:
            return number

        if base1 > 10:
            number = Conversions.successive_divisions(base1, 10, number)
        elif base1 < 10:
            number = Conversions.substitution(base1, 10, number)

        if base2 > 10:
            number = Conversions.substitution(10, base2, number)
        elif base2 < 10:
            number = Conversions.successive_divisions(10, base2, number)

        return number
