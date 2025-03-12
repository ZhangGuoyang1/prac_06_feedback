"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import Car


def main():
    # Create an initial car (for example, a used car with a name)
    used_car = Car(50, "UsedCar")
    print(used_car)

    # Create a new Car object called "limo" with 100 units of fuel and name it "Limo"
    limo = Car(100, "Limo")

    # Add 20 more units of fuel to limo
    limo.add(20)

    # Print the amount of fuel in limo (accessing the fuel attribute)
    print(f"{limo.name} fuel: {limo.fuel}")

    # Attempt to drive the limo 115 km
    distance_driven = limo.drive(115)
    print(f"{limo.name} drove {distance_driven} km")

    # Print the car object to see the updated __str__ output
    print(limo)


if __name__ == '__main__':
    main()

