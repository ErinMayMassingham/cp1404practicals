from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
taxi.start_fare()
taxi.drive(18)
print(taxi.get_fare())