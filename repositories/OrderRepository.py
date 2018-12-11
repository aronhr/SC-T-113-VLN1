import csv
import os
import datetime
from modules.order.order import Order
from repositories.CarRepository import CarRepository
import string
remove_punct_map = dict.fromkeys(map(ord, string.punctuation))


class OrderRepository(object):
    def __init__(self):
        self.__car_repo = CarRepository()

    @staticmethod
    def get_orders():
        try:
            with open("./data/order.csv", encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                orders = []
                for line in csv_reader:
                    orders.append(line)
                return orders
        except Exception:
            return ""

    @staticmethod
    def add_order(new_order, edit=False):
        kt = new_order.get_kt()
        name = new_order.get_renter()
        car = new_order.get_car()
        from_date = new_order.get_from_date()
        to_date = new_order.get_to_date()
        if not edit:
            from_date = datetime.datetime.strftime(from_date, "%d/%m/%y")
            to_date = datetime.datetime.strftime(to_date, "%d/%m/%y")

        price = new_order.get_price()
        insurance = new_order.get_insurance()
        total_price = new_order.get_price_insurance()
        days = new_order.get_days()
        with open("./data/order.csv", "a+", encoding='utf-8') as file:
            try:
                if os.stat("./data/order.csv").st_size == 0:
                    file.write("{},{},{},{},{},{},{},{},{}".format("Kt", "Name", "License", "From date", "To date", "Price", "Insurance", "Total price", "Days"))

                file.write("\n{},{},{},{},{},{},{},{},{}".format(kt, name, car, from_date, to_date, price, insurance, total_price, days))
            except Exception as e:
                print(e)

    def get_order_id(self, o_id):
        try:
            order = self.get_orders()
            return order[o_id]
        except IndexError:
            print("ID not available!")

    # noinspection PyTypeChecker
    def remove_order_id(self, o_id):
        try:
            orders = self.get_orders()
            selected_order = orders[o_id - 1]
            os.remove("./data/order.csv")
            for x in orders:
                if x == selected_order:
                    pass
                else:
                    new_order = Order(x["Kt"], x["Name"], x["License"], datetime.datetime.strptime(x["From date"], "%d/%m/%y"),
                                      datetime.datetime.strptime(x["To date"], "%d/%m/%y"), x["Price"], x["Insurance"],
                                      x["Total price"], x["Days"])
                    self.add_order(new_order)
        except Exception as e:
            print(e)

    def pay_order(self, price, order):
        action = ''
        while action != 'q':
            print("How do you want to pay?")
            print("1. Card")
            print("2. Cash")
            print("Press q to quit\n")
            print("Total Price: {}".format(price))
            action = input("Choose an option: ")

            if action == '1':
                payment_method = input('Debit or credit? ')
                self.add_complete_order_to_file(order, price, payment_method)
                return payment_method

            elif action == '2':
                payment_method = "Cash"
                self.add_complete_order_to_file(order, price, payment_method)
                return payment_method

    @staticmethod
    def add_complete_order_to_file(order, price, payment_method):
        with open("./data/completed_orders.csv", "a+", encoding='utf-8') as file:
            try:
                if os.stat("./data/completed_orders.csv").st_size == 0:
                    file.write("{},{},{},{},{},{},{},{},{},{}".format("Kt", "Name", "License", "From date", "To date", "Price",
                                                          "Payment method","Insurance","Total price","Days"))

                file.write(
                    "\n{},{},{},{},{},{},{},{},{},{}".format(order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                                                 price, payment_method, order["Insurance"],
                                                    order["Total price"], order["Days"]))
            except Exception as e:
                print(e)

    @staticmethod
    def get_completed_orders():
        try:
            with open("./data/completed_orders.csv", encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                orders = []
                for line in csv_reader:
                    orders.append(line)
                return orders
        except Exception:
            return "{}".format("No orders")

    def get_completed_order_id(self, o_id):
        try:
            order = self.get_completed_orders()
            return order[o_id]
        except IndexError:
            print("ID not available!")
