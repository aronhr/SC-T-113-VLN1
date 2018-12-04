import csv
import os
from modules.person.customer import Customer
import os


class CustomerRepository:
    def __init__(self):
        customers = []

    @staticmethod
    def get_customer():
        try:
            with open("./data/customers.csv", encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                arr = []
                for line in csv_reader:
                    arr.append(line)
                return arr
        except Exception:
            return "{}".format("No customers")

    @staticmethod
    def add_customer(customer):
        name = customer.get_name()
        kt = customer.get_kt()
        country = customer.get_country()
        address = customer.get_address()
        mail = customer.get_mail()
        phone_number = customer.get_phone_number()
        d_license = customer.get_license()
        age = customer.get_age()

        with open("./data/customers.csv", "a+", encoding='utf-8') as file:
            try:
                if os.stat("./data/customers.csv").st_size == 0:
                    file.write("{},{},{},{},{},{},{},{}".format("Name", "Passport number", "Country", "Address", "Mail",
                                                                "Phone number", "license", "Age"))

                file.write("\n{},{},{},{},{},{},{},{}".format(name, kt, country, address, mail, phone_number,
                                                              d_license, age))
            except Exception:
                print("lol")

    def get_customer_id(self, c_id):
        customer = self.get_customer()
        return customer[c_id]

    # noinspection PyTypeChecker
    def remove_customer(self, customer_id):
        customer = self.get_customer()
        selected_customer = customer[customer_id - 1]
        os.remove("./data/customers.csv")
        for x in customer:
            if x == selected_customer:
                pass
            else:
                new_customer = Customer(x["Name"], x["Passport number"], x["Country"], x["Address"], x["Mail"], x["Phone number"], x["license"], x["Age"])
                self.add_customer(new_customer)

    # noinspection PyTypeChecker
    def print_customer(self, customer_id):
        print("\nPassport number: {}".format(self.get_customer()[customer_id - 1]["Passport number"]))
        print("Name: {}".format(self.get_customer()[customer_id - 1]["Name"]))
        print("Country: {}".format(self.get_customer()[customer_id - 1]["Country"]))
        print("Address: {}".format(self.get_customer()[customer_id - 1]["Address"]))
        print("Phone number: {}".format(self.get_customer()[customer_id - 1]["Phone number"]))
        print("E-mail: {}".format(self.get_customer()[customer_id - 1]["Mail"]))
        print("Driver´s license: {}".format(self.get_customer()[customer_id - 1]["license"]))
        print("Age: {}".format(self.get_customer()[customer_id - 1]["Age"]))
        print("-" * 35)
