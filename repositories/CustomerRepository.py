import csv
import os
from modules.person.customer import Customer


class Customer:
    def __init__(self):
        customers = []

    @staticmethod
    def get_customer():
        try:
            with open("./data/customers.csv") as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
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

        with open("./data/customers.csv", "a+") as file:
            if os.stat("./data/customers.csv").st_size == 0:
                file.write("{},{},{},{},{},{},{},{}".format("Name", "Passport number", "Country", "Phone number", "Age", "Mail", "Address", "Driver´s license\n"))
            file.write("{},{},{},{},{},{},{},{}\n".format(name, kt, country, address, mail, phone_number, d_license, age))