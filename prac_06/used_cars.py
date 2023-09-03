"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from cp1404practicals.prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car("Limo", 100)
    # Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)
    # Print the amount of fuel in the car.
    print(f"{limo.name} has fuel: {limo.fuel}")
    # Attempt to drive the car 115 km using the drive method.
    limo.drive(115)
    print(limo)
    test_string = str(limo)
    print(test_string)

main()