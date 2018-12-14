from repositories.OrderRepository import OrderRepository
from repositories.CustomerRepository import CustomerRepository
import math


class OrderService:
    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__customer_repo = CustomerRepository()

    def check_kt(self, kt):
        return self.__customer_repo.check_if_kt_exist(kt)

    def add_order(self, new_order, edit):
        return self.__order_repo.add_order(new_order, edit)

    def get_orders(self):
        return self.__order_repo.get_orders()

    def get_order_by_id(self, o_id):
        return self.__order_repo.get_order_id(o_id - 1)

    def get_completed_order_id(self, o_id):
        return self.__order_repo.get_completed_order_id(o_id - 1)

    def remove_order(self, o_id):
        return self.__order_repo.remove_order_id(o_id)

    def pay_order(self, price, order):
        return self.__order_repo.pay_order(price, order)

    def get_completed_orders(self):
        return self.__order_repo.get_completed_orders()

    def get_available_orders(self, license):
        orders = self.__order_repo.get_completed_orders()
        if orders:
            order = []
            for x in orders:
                if x["License"] == license:
                    order.append(x)
            return order
        else:
            return False

    def get_available_order_customer(self, kt):
        """
        Gets available order by "kt"
        :param kt:
        :return:
        """
        orders = self.__order_repo.get_completed_orders()
        if orders:
            order = []
            for x in orders:
                if x["Kt"] == kt:
                    order.append(x)
            return order
        else:
            return False

    @staticmethod
    def next_list(stop):
        start = stop
        stop = start + 10
        return start, stop, start + 1

    @staticmethod
    def prev_list(start):
        stop = start
        start = stop - 10
        return start, stop, start + 1

    def print_current_orders(self, orders):
        """
        Prints out the currents order
        :param orders:
        :return:
        """
        start = 0
        stop = 10
        count = 1
        while True:
            print("{:^6}|{:^12}|{:^20}|{:^13}|{:^15}|{:^15}|{:^13}|{:^11}|{:^13}|{:^6}".format
                  ("ID", "PPN/Kt", "Name", "License", "From date", "To date", "Price", "Insurance", "Total price", "Days"))
            print("-" * 133)
            for ix, order in enumerate(orders[start:stop]):
                print("{:^8}{:<13}{:<21}{:<16}{:<16}{:<14}{:<14}{:<12}{:<14}{:<6}".format
                      (ix + count, order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                       order["Price"]+" kr.", order["Insurance"], order["Total price"]+" kr.", order["Days"]))
            print()
            y_n = input("Next / Previous / Quit searching (N/P/Q): ").lower()
            if y_n == "n" and count + 10 < len(orders):
                start, stop, count = self.next_list(stop)
            elif y_n == "n" and count + 10 >= len(orders):
                print("\nCant go forwards while on the last page\n")
            elif y_n == "p" and count != 1:
                start, stop, count = self.prev_list(start)
            elif y_n == 'p' and count == 1:
                print("\nCant go back while on the first page\n")
                continue
            elif y_n == 'q':
                return y_n
            else:
                print("\n\33[;31mWrong input, try again!\33[;0m\n")
                continue

    def print_completed_orders(self, completed_orders):
        """
        Prints out orders that are completed.
        :param completed_orders:
        :return:
        """
        start = 0
        stop = 10
        count = 1
        while True:
            print("{:^6}|{:^12}|{:^20}|{:^13}|{:^15}|{:^15}|{:^13}|{:^11}|{:^13}|{:^16}|{:^6}".format
                  ("ID", "PPN/Kt", "Name", "License", "From date", "To date", "Price", "Insurance",
                   "Total price", "Payment method", "Days"))

            print("-" * 150)
            for ix, order in enumerate(completed_orders[start:stop]):
                print("{:^8}{:<13}{:<21}{:<16}{:<16}{:<14}{:<14}{:<12}{:<14}{:<16}{:<6}".format
                      (ix + count, order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                       order["Price"]+" kr.", order["Insurance"], order["Total price"]+" kr.", order["Payment method"],order["Days"]))
            print()
            y_n = input("Next / Previous / Quit searching (N/P/Q): ").lower()
            if y_n == "n" and count + 10 < len(completed_orders):
                start, stop, count = self.next_list(stop)
            elif y_n == "n" and count + 10 >= len(completed_orders):
                print("\nCant go forwards while on the last page\n")
            elif y_n == "p" and count != 1:
                start, stop, count = self.prev_list(start)
            elif y_n == 'p' and count == 1:
                print("\nCant go back while on the first page\n")
                continue
            elif y_n == 'q':
                return y_n
            else:
                print("\n\33[;31mWrong input, try again!\33[;0m\n")
                continue
