from prac_08.taxi import Taxi


def main():
    taxi_prius = Taxi("Prius", 100)
    taxi_prius.drive(40)
    print(taxi_prius)
    taxi_prius.start_fare()
    taxi_prius.drive(100)
    print(taxi_prius)


main()
