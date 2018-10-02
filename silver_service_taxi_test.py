from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    silver_taxi = SilverServiceTaxi("Hummer", 100, 2)
    silver_taxi.drive(20)
    print(silver_taxi)
    print(silver_taxi.get_fare())
main()