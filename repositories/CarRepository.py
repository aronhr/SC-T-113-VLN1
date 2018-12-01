import csv
import os
from modules.car.Car import Car


class CarRepository(object):
    def __init__(self):
        pass

    def get_car(self):
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

    def add_car(self, car):
        model = car.get_model()
        cartype = car.get_type()
        carclass = car.get_class()
        seats = car.get_seats()
        fwd = car.get_4x4()
        transmission = car.get_transmission()

        with open("./data/car.csv", "a+") as file:
            if os.stat("./data/car.csv").st_size == 0:
                file.write("{},{},{},{},{},{},{}".format("Model", "Type", "Class", "Seats", "4x4", "Transmission", "Status"))

            file.write("\n{},{},{},{},{},{},{}".format(model, cartype, carclass, seats, fwd, transmission, False))

    def get_available_car(self):
        cars = self.get_car()
        available = []
        for x in cars:
            if x[6] == "True":
                available.append(x)
        return available

    def get_not_available_car(self):
        cars = self.get_car()
        not_available = []
        for x in cars:
            if x[6] == "False":
                not_available.append(x)
        return not_available
