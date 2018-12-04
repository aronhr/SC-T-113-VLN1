import csv
import os


class RentRepository(object):
    def __init__(self):
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
            return "{}".format("Add some rents to start with")