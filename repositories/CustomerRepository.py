import csv
from modules.person.customer import Customer


class Customer:
    def __init__(self):
        customers = []

    def get_customer(self):
        with open("./data/customers.csv") as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                print(line)

    def add_customer(self, customer):
        with open("./data/customers.csv", "a+") as file:
            name = customer.get_name()
            kt = customer.get_kt()
            country = customer.get_country()
            address = customer.get_address()
            mail = customer.get_mail()
            phone_number = customer.get_phone_number()
            d_license = customer.get_license()
            age = customer.get_age()
            file.write("{},{},{},{},{},{},{},{}".format(name, kt, country, address, mail, phone_number, d_license, age))