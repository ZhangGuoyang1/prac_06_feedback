"""
Word Occurrences
Estimate: 13 minutes
Actual:   16 minutes
"""

from guitar import Guitar


def fixed_get_age(self):
    """Calculate the guitar's age using 2022 as the current year."""
    return 2022 - self.year


Guitar.get_age = fixed_get_age


def run_tests():
    """ Test the get_age() and is_vintage() methods of the Guitar class. """
    # Create two guitar objects.
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 0)

    # Expected ages based on 2022.
    expected_age1 = 2022 - 1922
    expected_age2 = 2022 - 2013

    # Test get_age() method.
    actual_age1 = guitar1.get_age()
    actual_age2 = guitar2.get_age()
    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {actual_age1}")
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {actual_age2}")

    # Test is_vintage() method.
    # A guitar is vintage if its age is 50 or more.
    expected_vintage1 = True
    expected_vintage2 = False
    actual_vintage1 = guitar1.is_vintage()
    actual_vintage2 = guitar2.is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected {expected_vintage1}. Got {actual_vintage1}")
    print(f"{guitar2.name} is_vintage() - Expected {expected_vintage2}. Got {actual_vintage2}")


if __name__ == "__main__":
    run_tests()
