"""
Word Occurrences
Estimate: 25 minutes
Actual:   29 minutes
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, otherwise False."""
        # One simple way is to check if typing == "Dynamic"
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
