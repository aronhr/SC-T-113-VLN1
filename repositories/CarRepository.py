import csv
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
        with open("./data/car.csv", "a+") as file:
            id = car.get_id()
            model = car.get_model()
            cartype = car.get_type()
            carclass = car.get_class()
            seats = car.get_seats()
            fwd = car.get_4x4()
            transmission = car.get_transmission()
            file.write("{},{},{},{},{},{}\n".format(id, model, cartype, carclass, seats, fwd, transmission))
