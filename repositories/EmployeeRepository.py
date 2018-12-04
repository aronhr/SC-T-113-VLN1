import csv
import os

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
    def add_employee(employees):
        kennitala = employees.get_kt()
        fname = employees.get_fname()
        lname = employees.get_lname()
        email = employees.get_email()
        phone = employees.get_phone_number()
        with open("./data/employees.csv", "a+") as file:
            if os.stat("./data/employees.csv").st_size == 0:
                file.write("{},{},{},{},{}".format("Kt", "First name", "Last name", "Mail", "Phone_number"))
            file.write("\n{},{},{},{},{}".format(kennitala, fname, lname, email, phone))


