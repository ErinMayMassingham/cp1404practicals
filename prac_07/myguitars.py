from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Display guitars loaded from file"""
    print("These are the guitars loaded:")
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    guitars.sort()  # Uses __lt__ method in Guitar class
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

def load_guitars(filename):
    """Load guitars from CSV into a list of Guitars"""
    guitars = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    """Print all guitars in list"""
    for i, guitar in enumerate(guitars, start=1):
        print(f"Guitar {i}: {guitar}")


main()
