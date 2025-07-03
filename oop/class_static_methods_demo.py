# class_static_methods_demo.py

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        It does not access any class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that returns the product of two numbers.
        It accesses the class attribute 'calculation_type' using the 'cls' parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b