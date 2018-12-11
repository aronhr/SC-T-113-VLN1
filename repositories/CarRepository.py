import csv
import os
from modules.car.Car import Car
import datetime


class CarRepository(object):
    def __init__(self):
        pass

    @staticmethod
    def get_car():
        try:
            with open("./data/car.csv") as file:
                csv_reader = csv.DictReader(file)
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
        status = car.get_status()
        license = car.get_license()

        with open("./data/car.csv", "a+") as file:
            if os.stat("./data/car.csv").st_size == 0:
                file.write("{},{},{},{},{},{},{},{},{}".format("Model", "Type", "Class", "Seats", "4x4", "Transmission",
                                                               "Status", "Price", "License"))
            file.write(
                "\n{},{},{},{},{},{},{},{},{}".format(model, cartype, carclass, seats, fwd, transmission, status, price,
                                                      license))

    # noinspection PyTypeChecker
    def get_available_car(self, t):  # t stendur fyrir annað hvort True eða False
        car = self.get_car()
        cars = []
        for x in car:
            if x["Status"] == t:
                cars.append(x)
        return cars

    def get_available_date_car(self, from_date, to_date):
        try:
            with open("./data/order.csv") as file:
                csv_reader = csv.DictReader(file)
                cars = []
                for line in csv_reader:
                    if datetime.datetime.strptime(line["From date"], "%d/%m/%y") <= from_date <= datetime.datetime.strptime(
                            line["To date"], "%d/%m/%y") or datetime.datetime.strptime(line["From date"],
                                                                                       "%d/%m/%y") <= to_date <= datetime.datetime.strptime(
                            line["To date"], "%d/%m/%y"):
                        cars.append(line)
                return cars
        except FileNotFoundError:
            self.get_car()

    def get_car_id(self, id):
        car = self.get_car()
        return car[id]

    # noinspection PyTypeChecker
    def remove_car_id(self, id):
        car = self.get_car()
        selected_car = car[id - 1]
        os.remove("./data/car.csv")
        for x in car:
            if x == selected_car:
                pass
            else:
                new_car = Car(x["Model"], x["Type"], x["Class"], x["Seats"], x["4x4"], x["Transmission"], x["License"],
                              int(x["Price"]), x["Status"])
                self.add_car(new_car)
