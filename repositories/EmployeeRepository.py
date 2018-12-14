import csv
import os
from modules.person.Employee import Employee


class EmployeeRepository(object):
    def __init__(self):
        pass

    def check_if_kt_exist(self, kt):
        """
        Checks is the kt is in (get employee) and returns a "false" or "true"
        :param kt:
        :return:
        """
        data = self.get_employee()
        if data:
            for x in data:
                if x["Passport number"] == kt:
                    return x
            else:
                return False
        else:
            return False

    @staticmethod
    def get_employee():
        """
        gets all employees, and appends it in to a lists and returns it.
        :return:
        """
        try:
            with open("./data/employees.csv", encoding="utf-8") as file:
                csv_reader = csv.DictReader(file)
                # next(csv_reader)
                employees = []
                for line in csv_reader:
                    employees.append(line)
                return employees
        except Exception:
            return False

    @staticmethod
    def add_employee(customer):
        """
        adds an employee, and appends that specific employee that the customer created.
        :param customer:
        :return:
        """
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
                print("Error adding employee to file")

    def get_employee_id(self, id):
        """
        Gets the employee by id, and the returns the specific employee.
        :param id:
        :return:
        """
        try:
            emp = self.get_employee()
            return emp[id]
        except Exception:
            return False

    def remove_employee_id(self, id):
        """
        Removes the employee by id, we use the get_employee() function to help us getting the employee
        then we delete the employee csv file, then we build the csv file again without the deleted employee.
        :param id:
        :return:
        """
        try:
            emp = self.get_employee()
            selected_emp = emp[id - 1]
            os.remove("./data/employees.csv")

            for x in emp:
                if x == selected_emp:
                    pass
                else:
                    new_employee = Employee(x["Name"], x["Passport number"], x["Country"], x["Address"], x["Mail"], x["Phone number"],
                                  int(x["license"]), x["Age"])
                    self.add_employee(new_employee)
        except Exception:
            return False

