import csv
import os
from modules.person.Employee import Employee


class EmployeeRepository(object):
    def __init__(self):
        pass

    @staticmethod
    def get_employee():
        try:
            with open("./data/employees.csv") as file:
                csv_reader = csv.DictReader(file)

                # next(csv_reader)
                employees = []
                for line in csv_reader:
                    employees.append(line)
                return employees
        except Exception:
            return "{}".format("Add some employee")

    @staticmethod
    def add_employee(customer):
        name = customer.get_name()
        kt = customer.get_kt()
        country = customer.get_country()
        address = customer.get_address()
        mail = customer.get_mail()
        phone_number = customer.get_phone_number()
        d_license = customer.get_license()
        age = customer.get_age()

        with open("./data/employees.csv", "a+", encoding='utf-8') as file:
            try:
                if os.stat("./data/employees.csv").st_size == 0:
                    file.write("{},{},{},{},{},{},{},{}".format("Name", "Passport number", "Country", "Address", "Mail",
                                                                "Phone number", "license", "Age"))

                file.write("\n{},{},{},{},{},{},{},{}".format(name, kt, country, address, mail, phone_number,
                                                              d_license, age))
            except Exception:
                print("lol")

