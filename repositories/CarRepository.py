import csv
import os
from modules.car.Car import Car


class CarRepository:
    def __init__(self):
        cars = []

    def get_car(self):
        # TODO: Make table
        with open("./data/car.csv") as file:
            csv_reader = csv.reader(file)

            next(csv_reader)

            for line in csv_reader:
                print(line)

    def add_car(self, car):
        model = car.get_model()
        cartype = car.get_type()
        carclass = car.get_class()
        seats = car.get_seats()
        fwd = car.get_4x4()
        transmission = car.get_transmission()
        with open("./data/car.csv", "a+") as file:
            if os.stat("./data/car.csv").st_size == 0:
                file.write("{},{},{},{},{},{},{}\n".format("id", "model", "type", "class", "seats", "4x4", "transmission"))
            file.write("{},{},{},{},{},{}\n".format(model, cartype, carclass, seats, fwd, transmission))
