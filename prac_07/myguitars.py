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

    new_guitars = add_guitars()
    guitars.extend(new_guitars)

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

def add_guitars():
    """Ask user to enter new guitars adn return list of Guitars"""
    new_guitars = []
    print("\nAdd your new guitars:")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars


main()
