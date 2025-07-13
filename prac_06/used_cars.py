"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.

Expected time: 15
Total Time:
"""

from prac_06.car import Car

def main():
    """Demo test code to show how to use Car class."""

    # Original test car (now with a name)
    my_car = Car("MyCar", 180)
    my_car.drive(30)
    print(f"{my_car.name} has fuel: {my_car.fuel}")
    print(my_car)

    # New Limo car object
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"{limo.name} has fuel: {limo.fuel}")# Print the amount of fuel after adding
    distance_driven = limo.drive(115) # Attempt to drive 115 km
    print(f"{limo.name} drove {distance_driven} km")

    # Final car state using __str__
    print(limo)

main()