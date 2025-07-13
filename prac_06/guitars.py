"""
Expected time: 20 mins
Total Time: 35 mins
"""
from prac_06.guitar import Guitar

def main():
    """Get guitars from user and display them with vintage status."""
    print("My guitars!")
    guitars = get_guitars()

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_tag = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_tag}")

def get_guitars():
    """User enter guitar details and return a list of guitar objects."""
    guitars = []
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")
    return guitars

if __name__ == "__main__":
    main()