"""Band class for CP1404"""

class Band:
    """Represent a band, composed of musicians."""

    def __init__(self, name):
        """Initialize the band with its name."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band."""
        musician_strings = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Play the band."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)
