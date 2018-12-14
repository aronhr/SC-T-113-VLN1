from repositories.CustomerRepository import CustomerRepository
import math


class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

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

    def print_customers(self, customers):
        """
        Prints all the customers that we have.
        :param customers:
        :return:
        """
        start = 0
        stop = 10
        count = 1
        while True:
            print("{:^6}|{:^18}|{:^17}|{:^11}|{:^17}|{:^30}|{:^14}|{:^18}|{:^5}|".format
                  ("ID", "Name", "Passport number", "Country", "Address", "E-mail", "Phone number", "Driving license",
                   "Age"))
            print("-" * 145)
            for ix, customer in enumerate(customers[start:stop]):
                print("{:^8}{:<19}{:<18}{:<12}{:<18}{:<31}{:<15}{:<19}{:<7}".format(ix + count, customer["Name"], customer[
                    "Passport number"], customer["Country"], customer["Address"], customer["Mail"],
                                                                                    customer["Phone number"],
                                                                                    customer["license"], customer["Age"]))
            print()
            y_n = input("Next / Previous / Quit searching (N/P/Q): ").lower()
            if y_n == "n" and count <= math.ceil(len(customers) / 2):
                start, stop, count = self.next_list(stop)
            elif y_n == "n" and count > math.ceil(len(customers) / 2):
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

    def list_all_customers(self):
        """
        List all the customers by using the get_customer(),
         and returns a message if there is no customers
        :return:
        """
        customers = self.get_customers()
        if customers:
            self.print_customers(customers)
        else:
            print("No customers\n")

    # noinspection PyTypeChecker
    @staticmethod
    def print_customer(customer):
        """
        Prints a specific customer.
        :param customer:
        :return:
        """
        print("\tPPN/Kt: {}".format(customer["Passport number"]))
        print("\tName: {}".format(customer["Name"]))
        print("\tCountry: {}".format(customer["Country"]))
        print("\tAddress: {}".format(customer["Address"]))
        print("\tPhone number: {}".format(customer["Phone number"]))
        print("\tE-mail: {}".format(customer["Mail"]))
        print("\tDriver´s license: {}".format(customer["license"]))
        print("\tAge: {}".format(customer["Age"]))

    def add_customer(self, customer):

        self.__customer_repo.add_customer(customer)

    def get_customers(self):
        return self.__customer_repo.get_customer()

    def get_customer_by_kt(self, kt):
        """
        Get a customer by the Passport Number or kt
        :param kt:
        :return:
        """
        customers = self.get_customers()
        for x in customers:
            if x["Passport number"] == kt:
                return x
        return 0

    def remove_customer(self, customer_id):

        return self.__customer_repo.remove_customer(customer_id)

    def get_customer_by_id(self, c_id):
        return self.__customer_repo.get_customer_id(c_id - 1)
