import csv
import os
from modules.person.customer import Customer


class Customer:
    def __init__(self):
        customers = []

    @staticmethod
    def get_customer():
        try:
            with open("./data/customers.csv", encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
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

        with open("./data/customers.csv", "a+", encoding='utf-8') as file:
            if os.stat("./data/customers.csv").st_size == 0:
                file.write("{},{},{},{},{},{},{},{}".format("Name", "Passport number", "Country", "Phone number",
                                                            "Age", "Mail", "Address", "license"))
            else:
                file.write("\n{},{},{},{},{},{},{},{}".format(name, kt, country, address, mail, phone_number,
                                                              d_license, age))

    def edit_customer(self, customer_id):
        action = ''
        print(self.get_customer()[customer_id - 1])

        while action != '9':
            print("1. Passport number")
            print("2. Name")
            print("3. Country")
            print("4. Address")
            print("5. Phone number")
            print("6. E-mail")
            print("7. Driver´s license")
            print("8. Age")
            print("9. Go back")
            action = input("What to you want to edit: ?").lower()

            if action == '1':
                customer = self.get_customer()[customer_id - 1]
                with open("./data/customers.csv", encoding='utf-8') as file:
                    line = file.readlines()
                    print(line[1])
                   # lines = list(file)
                  #  print(lines)
                 #   print(lines[customer_id - 1][1])
                   # lines[customer_id - 1][1] = input("Enter new passport number: ")
             #   print(customer.items())
