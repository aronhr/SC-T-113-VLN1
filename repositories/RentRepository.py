import csv
import os


class RentRepository(object):
    def __init__(self):
        pass

    def check_if_kt_exist(self, kt):
        try:
            with open("./data/rent.csv") as file:
                pass
        except Exception:
            pass

    def get_rent(self):
        try:
            with open("./data/rent.csv") as file:
                csv_reader = csv.reader(file)

                next(csv_reader)
                rent = []
                for line in csv_reader:
                    rent.append(line)
                return rent
        except Exception:
            return "{}".format("Add some cars to start with")

    @staticmethod
    def add_rent(rent):

        with open("./data/car.csv", "a+") as file:
            # if os.stat("./data/car.csv").st_size == 0:
             #   file.write("{},{},{},{},{},{},{},{}".format("Model", "Type", "Class", "Seats", "4x4", "Transmission",
              #                                              "Status", "Price per day"))
            pass
            # file.write("\n{},{},{},{},{},{},{},{}".format(model, cartype, carclass, seats, fwd, transmission, True, price))

    def get_available_rent(self, t):     # t stendur fyrir annaðhvort True eða False
        car = self.get_rent()
        cars = []
        for x in car:
            if x[6] == t:
                cars.append(x)
        return cars

    def get_rent_id(self, id):
        car = self.get_rent()
        return car[id - 1]

    def remove_rent_id(self, id):
        pass
        # car = self.get_car()
        # return car[id - 1]
