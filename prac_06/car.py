"""CP1404/CP5632 Practical - Car class example.
Expected time: 20
Total Time: 15
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise Car
        name: str, name of car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a distance.

        Drive distance if car has enough fuel or drive until fuel runs out, return distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """Return string rep of car"""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"