import csv
import os
import datetime
from modules.order.order import Order


class OrderRepository(object):
    def __init__(self):
        pass

    @staticmethod
    def get_orders():
        try:
            with open("./data/order.csv") as file:
                csv_reader = csv.DictReader(file)
                rent = []
                for line in csv_reader:
                    rent.append(line)
                return rent
        except Exception:
            return "{}".format("No orders")

    def add_order(self, new_order):
        name = new_order.get_renter()
        car = new_order.get_car()
        from_date = new_order.get_from_date()
        from_date = datetime.datetime.strftime(from_date, "%d/%m/%y")
        to_date = new_order.get_to_date()
        to_date = datetime.datetime.strftime(to_date, "%d/%m/%y")
        with open("./data/order.csv", "a+", encoding='utf-8') as file:
            try:
                if os.stat("./data/order.csv").st_size == 0:
                    file.write("{},{},{},{}".format("Name", "License", "From date", "To date"))

                file.write("\n{},{},{},{}".format(name, car, from_date, to_date))
            except Exception as e:
                print(e)