from prac_09.taxi import Taxi

def main():
    """Run a basic test of Taxi class functionality."""
    #Create a taxi object with name, fuel, and default class price_per_km
    my_taxi = Taxi("Prius 1", 100)

    #Drive the taxi 40km
    my_taxi.drive(40)

    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    #Restart the fare and drive another 100km
    my_taxi.start_fare()
    my_taxi.drive(100)

    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()
