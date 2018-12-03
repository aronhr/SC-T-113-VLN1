import csv
import os


class CarRepository(object):
    def __init__(self):
        pass

    @staticmethod
    def get_car():
        try:
            with open("./data/car.csv") as file:
                csv_reader = csv.reader(file)

                next(csv_reader)
                cars = []
                for line in csv_reader:
                    cars.append(line)
                return cars
        except Exception:
            return "{}".format("Add some cars to start with")

    @staticmethod
    def add_car(car):
        model = car.get_model()
        cartype = car.get_type()
        carclass = car.get_class()
        seats = car.get_seats()
        fwd = car.get_4x4()
        transmission = car.get_transmission()

        with open("./data/car.csv", "a+") as file:
            if os.stat("./data/car.csv").st_size == 0:
                file.write("{},{},{},{},{},{},{}".format("Model", "Type", "Class", "Seats", "4x4", "Transmission", "Status"))

            file.write("\n{},{},{},{},{},{},{}".format(model, cartype, carclass, seats, fwd, transmission, True))

    def get_available_car(self, t):     # t stendur fyrir annaðhvort True eða False
        car = self.get_car()
        cars = []
        for x in car:
            if x[6] == t:
                cars.append(x)
        return cars
