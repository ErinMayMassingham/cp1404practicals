"""CP1404 Prac 7 Projects"""

class Project:
    """Class to represent a project with details"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date  # string for now
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string representation of a project"""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def is_complete(self):
        """Check if project is fully completed"""
        return self.completion_percentage >= 100

    def get_start_date(self):
        """"Get start date of project"""
        return datetime.strptime(self.start_date, "%d/%m/%Y").date()