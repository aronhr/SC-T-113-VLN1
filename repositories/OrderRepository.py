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
            with open("./data/order.csv", encoding='utf-8') as file:
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

    def get_order_id(self, o_id):
        try:
            order = self.get_orders()
            return order[o_id]
        except IndexError:
            print("ID not available!")

    def remove_order_id(self, o_id):
        try:
            orders = self.get_orders()
            selected_order = orders[o_id-1]
            os.remove("./data/order.csv")
            for x in orders:
                if x == selected_order:
                    pass
                else:
                    new_order = Order(x["Name"], x["License"], datetime.datetime.strptime(x["From date"], "%d/%m/%y"), datetime.datetime.strptime(x["To date"], "%d/%m/%y"))
                    self.add_order(new_order)
        except Exception as e:
            print(e)
