"""
Expected time: 20 mins
Total Time: 23 mins
"""
VINTAGE_AGE = 50


class Guitar:
    """Class for storing details of guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        from datetime import date
        return date.today().year - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE