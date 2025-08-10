from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")
    print(MENU)

    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, fanciness=2),
        SilverServiceTaxi("Hummer", 200, fanciness=4)
    ]
    current_taxi = None
    total_bill = 0

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(current_taxi, taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi, total_bill):
    distance = float(input("Drive how far? "))
    current_taxi.start_fare()
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    total_bill += trip_cost
    return total_bill


def choose_taxi(current_taxi, taxis):
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
    return current_taxi

def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()

