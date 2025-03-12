"""
Word Occurrences
Estimate: 16 minutes
Actual:   15 minutes
"""

from guitar import Guitar


def main():
    """ Collect guitars from user input and display their details."""
    guitars = []
    print("My guitars!")

    name = input("Name: ")

    while name != "":
        try:
            year = int(input("Year: "))
        except ValueError:
            print("Invalid year. Please enter an integer.")
            name = input("Name: ")
            continue
        try:
            cost = float(input("Cost: $"))
        except ValueError:
            print("Invalid cost. Please enter a number.")
            name = input("Name: ")
            continue

        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

        name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_str = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_str}")


if __name__ == "__main__":
    main()
