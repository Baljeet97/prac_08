from prac_08.unreliable_car import UnreliableCar


def main():
    reliable_car = UnreliableCar("Good", 80, 60)
    unreliable_car = UnreliableCar("dodgy", 80, 6)

    for i in range(1, 12):
        print("{:10} drove {:2}Km".format(reliable_car.name, reliable_car.drive(i)))
        print("{:10} drove {:2}Km".format(unreliable_car.name, unreliable_car.drive(i)))
    print(reliable_car)
    print(unreliable_car)


main()
