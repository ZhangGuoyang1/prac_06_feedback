"""CP1404/CP5632 Practical - Car class example."""


class Car:
    def __init__(self, fuel, name="Car"):
        self.fuel = fuel
        self.name = name
        self.odometer = 0

    def drive(self, km):
        # Drive as far as possible if there's not enough fuel.
        if km <= self.fuel:
            self.odometer += km
            self.fuel -= km
            return km
        else:
            distance_driven = self.fuel
            self.odometer += distance_driven
            self.fuel = 0
            return distance_driven

    def add(self, fuel):
        self.fuel += fuel

    def __str__(self):
        # Return a formatted string with the car's name, fuel and odometer reading.
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"
