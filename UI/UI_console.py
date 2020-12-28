"""

Susciuc Anastasia

"""
class UI:

    def __init__(self, service):
        self.__service = service
        self.commands = {'1': self.__ui_add,
                         '2': self.__ui_subtract,
                         '3': self.__ui_multiply,
                         '4': self.__ui_divide,
                         '5': self.__ui_substitution_method,
                         '6': self.__ui_successive_divisions,
                         '7': self.__ui_rapid_conversions,
                         '8': self.__ui_intermediate_base}

    def __ui_add(self):
        base = input("Insert the base to perform the addition (an integer from {2, 3, ..., 9, 10, 16}) :")
        first = input("Insert the first number:")
        second = input("Insert the second number:")

        res = self.__service.add(base, first, second)
        print(res)

    def __ui_subtract(self):
        base = input("Insert the base to perform the subtraction (an integer from {2, 3, ..., 9, 10, 16}) :")
        first = input("Insert the first number:")
        second = input("Insert the second number:")

        res = self.__service.subtract(base, first, second)
        print(res)

    def __ui_multiply(self):
        base = input("Insert the base to perform the multiplication (an integer from {2, 3, ..., 9, 10, 16}) :")
        first = input("Insert the first number:")
        second = input("Insert the second number:")

        res = self.__service.multiply(base, first, second)
        print(res)

    def __ui_divide(self):
        base = input("Insert the base to perform the division (an integer from {2, 3, ..., 9, 10, 16}) :")
        first = input("Insert the first number:")
        second = input("Insert the second number:")
        try:
            res, rem = self.__service.divide(base, first, second)
            print(res, "remainder", rem)
        except ValueError as ve:
            print(ve)

    def __ui_substitution_method(self):
        print("The number to be converted:")
        base1 = input("\tInsert its base (an integer from {2, 3, ..., 9, 10, 16}) :")
        num1 = input("\tInsert the number:")

        base2 = input("Insert the base to convert (an integer from {2, 3, ..., 9, 10, 16}) :")
        res = self.__service.substitution(base1, num1, base2)
        print(res)

    def __ui_successive_divisions(self):
        print("The number to be converted:")
        base1 = input("\tInsert its base (an integer from {2, 3, ..., 9, 10, 16}) :")
        num1 = input("\tInsert the number:")

        base2 = input("Insert the base to convert (an integer from {2, 3, ..., 9, 10, 16}) :")
        # print(base1, base2)
        res = self.__service.divisions(base1, num1, base2)
        print(res)

    def __ui_rapid_conversions(self):
        print("The number to be converted:")
        base1 = input("\tInsert its base (an integer from {2, 4, 8, 16}) :")
        num1 = input("\tInsert the number:")

        base2 = input("Insert the base to convert (an integer from {2, 4, 8, 16}) :")
        res = self.__service.rapid(base1, num1, base2)
        print(res)

    def __ui_intermediate_base(self):
        print("The number to be converted:")
        base1 = input("\tInsert its base (an integer from {2, 3, ..., 9, 10, 16}) :")
        num1 = input("\tInsert the number:")

        base2 = input("Insert the base to convert (an integer from {2, 3, ..., 9, 10, 16}) :")
        res = self.__service.intermediate(base1, num1, base2)
        print(res)

    @staticmethod
    def __print_menu():
        print("_______________________________________________")
        print("|  0. Exit the application                     |")
        print("|  1. Add two numbers                          |")
        print("|  2. Subtract two numbers                     |")
        print("|  3. Multiply two numbers                     |")
        print("|  4. Divide two numbers                       |")
        print("|  5. Conversion using substitution method     |")
        print("|  6. Conversion using successive divisions    |")
        print("|  7. Conversion using rapid conversions       |")
        print("|  8. Conversion using 10 as intermediate base |")
        print("|_________________________Anastasia Susciuc___ |")

    def run(self):
        while True:
            self.__print_menu()
            command = input("insert your command:")

            if command == '0':
                break

            if command not in self.commands:
                print("Invalid command!")
            else:
                try:
                    self.commands[command]()
                except ValueError as ve:
                    print(ve)
