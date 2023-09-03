"""CP1404/CP5632 Practical - Car class example."""


class Car:

    def __init__(self, name="", fuel=0):

        """Initialise a Car instance. """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def __str__(self):
        """Return a string representation of a Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance