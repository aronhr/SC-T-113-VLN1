import csv
from modules.person.customer import Customer
import os


class CustomerRepository:
    def __init__(self):
        customers = []

    def get_customer(self):
        with open("./data/customers.csv") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            arr = []
            for line in csv_reader:
                arr.append(line)
            return arr

    def add_customer(self, customer):
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
                file.write("{},{},{},{},{},{},{},{}".format("Name", "Kt", "Country", "Address", "Mail", "Phone_number", "License", "Age"))
            file.write("\n{},{},{},{},{},{},{},{}".format(name, kt, country, address, mail, phone_number, d_license, age))

    def check_if_kt_exist(self, kt):
        data = self.get_customer()
        for x in data:
            if x[1] == kt:
                return x
        else:
            return False
