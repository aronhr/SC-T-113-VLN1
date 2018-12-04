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
        price = car.get_price()

        with open("./data/car.csv", "a+") as file:
            if os.stat("./data/car.csv").st_size == 0:
                file.write("{},{},{},{},{},{},{},{}".format("Model", "Type", "Class", "Seats", "4x4", "Transmission",
                                                            "Status", "Price per day"))

            file.write("\n{},{},{},{},{},{},{},{}".format(model, cartype, carclass, seats, fwd, transmission, True, price))

    def get_available_car(self, t):     # t stendur fyrir annaðhvort True eða False
        car = self.get_car()
        cars = []
        for x in car:
            if x[6] == t:
                cars.append(x)
        return cars

    def get_car_id(self, id):
        car = self.get_car()
        return car[id]

    def remove_car_id(self, id):
        car = self.get_car()
        pass

