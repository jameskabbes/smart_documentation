"""
basic_operations.py
====================================
Module for simple math operations.
"""

class BasicOperations:
    """A class with some basic math operations."""

    def add(self, a, b) -> float:
        """
        Adds two numbers.

        :param kind: two numbers to be subtracted.
        :type kind: float, float
        :raise basic_operations.IncompatibleTypes: If the kind is invalid.
        :return: addition of two numbers.
        :rtype: float.
        """
        return a + b

    def subtract(self, a, b) -> float:
        """
        Subtracts two numbers.

        :param kind: two numbers to be subtracted.
        :type kind: float, float
        :raise basic_operations.IncompatibleTypes: If the kind is invalid.
        :return: subtraction of two numbers.
        :rtype: float.
        """
        return a - b

    def multiply(self, a, b) -> float:
        """
        Multiplies two numbers.

        :param kind: two numbers to be multiplied.
        :type kind: float, float
        :raise basic_operations.IncompatibleTypes: If the kind is invalid.
        :return: multiplication of two numbers.
        :rtype: float.
        """
        return a * b

    def divide(self, a, b) -> float:
        """
        Divides two numbers.

        :param kind: two numbers to be divided.
        :type kind: float, float
        :raise basic_operations.IncompatibleTypes: If the kind is invalid.
        :return: division of two numbers.
        :rtype: float.
        """
        return a / b

class IncompatibleTypes(Exception):
    """Raised if the two operands are incompatible."""
    pass