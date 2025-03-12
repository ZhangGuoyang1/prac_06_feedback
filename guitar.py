"""
Word Occurrences
Estimate: 15 minutes
Actual:   18 minutes
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Create a new Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ Return the guitar as a formatted string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate the guitar's age."""
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Check if the guitar is vintage (50 years or older)"""
        return self.get_age() >= 50


if __name__ == "__main__":
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(guitar)
    print("Age:", guitar.get_age())
    print("Vintage:", guitar.is_vintage())

