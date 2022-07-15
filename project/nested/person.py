"""
person.py
====================================
Module for representing individual people.
"""

def introduce_me(your_name):
    """
    Introduce yourself to the world.

    :param kind: name to be introduced.
    :type kind: string
    :return: an introductory message.
    :rtype: string.
    """
    return "The wise {} loves Python.".format(your_name)

class Person:
    """A class that defines a person object."""

    def __init__(self, name):
        self.name = name

    def about_me(self):
        """
        Return information about an instance created from the Person class.
        """
        return "I am a very smart {} object.".format(self.name)