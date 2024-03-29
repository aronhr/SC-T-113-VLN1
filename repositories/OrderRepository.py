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
        """
        Get all orders from the csv file, "order.csv"
        :return:
        """
        try:
            with open("./data/order.csv", encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                orders = []
                for line in csv_reader:
                    orders.append(line)
                return orders
        except Exception:
            return False

    @staticmethod
    def add_order(new_order, edit=False):
        """
        Here we create an order and we add it in to the csv file.
        :param new_order:
        :param edit:
        :return:
        """
        kt = new_order.get_kt()
        name = new_order.get_renter()
        car = new_order.get_car()
        from_date = new_order.get_from_date()
        to_date = new_order.get_to_date()
        if not edit:
            from_date = datetime.datetime.strftime(from_date, "%d/%m/%y")
            to_date = datetime.datetime.strftime(to_date, "%d/%m/%y")

        price = int(new_order.get_price())
        insurance = new_order.get_insurance()
        total_price = int(new_order.get_price_insurance())
        days = new_order.get_days()
        penalty = new_order.get_penalty()
        with open("./data/order.csv", "a+", encoding='utf-8') as file:
            try:
                if os.stat("./data/order.csv").st_size == 0:
                    file.write(
                        "{},{},{},{},{},{},{},{},{},{}".format("Kt", "Name", "License", "From date", "To date", "Price",
                                                               "Insurance", "Total price", "Days", "Penalty"))

                file.write("\n{},{},{},{},{},{},{},{},{},{}".format(kt, name, car, from_date, to_date, price, insurance,
                                                                    total_price, days, penalty))
            except Exception:
                print("Error adding order to file")

    def get_order_id(self, o_id):
        """
        We get specific orders by id, we use the get orders to help us. the we get the order by ID.
        :param o_id:
        :return:
        """
        try:
            order = self.get_orders()
            return order[o_id]
        except IndexError:
            return False

    # noinspection PyTypeChecker
    def remove_order_id(self, o_id):
        """
        Here we get all orders, we remove a specific order with id, the csv content deleted
        then the content will appear again without the specific order
        :param o_id:
        :return:
        """
        try:
            orders = self.get_orders()
            selected_order = orders[int(o_id) - 1]
            os.remove("./data/order.csv")
            for x in orders:
                if x == selected_order:
                    pass
                else:
                    new_order = Order(x["Kt"], x["Name"], x["License"],
                                      datetime.datetime.strptime(x["From date"], "%d/%m/%y"),
                                      datetime.datetime.strptime(x["To date"], "%d/%m/%y"), x["Price"], x["Insurance"],
                                      x["Total price"], x["Days"], x["Penalty"])
                    self.add_order(new_order)
        except Exception:
            print("Error removing order from file")

    def pay_order(self, price, order):
        """
        takes in how to will pay, and calls the add_complete_order_to_file and add the order in to the csv file.
        :param price:
        :param order:
        :return:
        """
        action = ''
        while action != 'q':
            print("How do you want to pay?")
            print("1. Card")
            print("2. Cash")
            print("Press q to quit\n")
            action = input("Choose an option: ").lower()
            if action == 'q':
                break
            if action == '1':
                payment_method = input('Debit or credit? ')
            elif action == '2':
                payment_method = "Cash"
            try:
                self.add_complete_order_to_file(order, price, payment_method)
                return payment_method
            except Exception:
                return False

    @staticmethod
    def add_complete_order_to_file(order, price, payment_method):
        """
        appends the order in to the csv file.
        :param order:
        :param price:
        :param payment_method:
        :return:
        """
        with open("./data/completed_orders.csv", "a+", encoding='utf-8') as file:
            try:
                if os.stat("./data/completed_orders.csv").st_size == 0:
                    file.write(
                        "{},{},{},{},{},{},{},{},{},{},{}".format("Kt", "Name", "License", "From date", "To date",
                                                                  "Price",
                                                                  "Payment method", "Insurance", "Total price", "Days",
                                                                  "Penalty"))

                file.write(
                    "\n{},{},{},{},{},{},{},{},{},{},{}".format(order["Kt"], order["Name"], order["License"],
                                                                order["From date"], order["To date"],
                                                                int(price), payment_method, order["Insurance"],
                                                                int(order["Total price"]), order["Days"],
                                                                order["Penalty"]))
            except Exception as e:
                print("Error adding complete order to file")

    @staticmethod
    def get_completed_orders():
        """
        Gets all the orders that have been used(completed),in the csv file.
        :return:
        """
        try:
            with open("./data/completed_orders.csv", encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                orders = []
                for line in csv_reader:
                    orders.append(line)
                return orders
        except FileNotFoundError:
            return False

    def get_completed_order_id(self, o_id):
        """
        Gets all the completed order by the id,
        we user the completed order to help us with is function
        :param o_id:
        :return:
        """
        try:
            order = self.get_completed_orders()
            return order[o_id]
        except IndexError:
            return False
