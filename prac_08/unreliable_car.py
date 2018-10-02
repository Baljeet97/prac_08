from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, driving):
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            driving = 0
        distance_driven = super().drive(driving)
        return distance_driven