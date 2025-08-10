import random
from prac_09.car import Car


class UnreliableCar(Car):
    """UnreliableCar is subclass where car may not run every time"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car based on reliability percentage."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0  # Car refused to move!
