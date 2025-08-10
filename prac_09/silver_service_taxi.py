from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A more luxurious Taxi with higher pricing and a flagfall charge."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # Custom instance variable

    def get_fare(self):
        """Return the fare, rounded to nearest 10c."""
        base_fare = super().get_fare()
        return round(base_fare + self.flagfall, 1)

    def __str__(self):
        """Return string representation"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
