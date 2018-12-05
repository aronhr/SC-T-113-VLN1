from services.EmployeeService import EmployeeService
from modules.person.Employee import Employee
import string

class EmployeeUI:
    def __init__(self):
        self.__employee_service = EmployeeService()

    def print_employees(self, emp):
        if self.__employee_service.get_employees() == "No customers":
            print("No customers")
        else:
            print(
                "{:^6}|{:^12}|{:^17}|{:^11}|{:^17}|{:^22}|{:^14}|{:^18}|{:^5}|".format("ID", "Name", "Passport number",
                                                                                       "Country", "Address", "E-mail",
                                                                                       "Phone number",
                                                                                       "Driver´s license",
                                                                                       "Age"))
            print("-" * 131)
            for ix, customer in enumerate(emp):
                print("{:^8}{:<13}{:<18}{:<12}{:<18}{:<23}{:<15}{:<19}{:<7}".format(ix + 1, customer["Name"], customer[
                    "Passport number"], customer["Country"], customer["Address"], customer["Mail"],
                                                                                    customer["Phone number"],
                                                                                    customer["license"],
                                                                                    customer["Age"]))
        print()

    def main_menu(self):
        action = ""
        while action != 'q':
            print("You can do the following: ")
            print("1. Add a employee")
            print("2. List all employees")
            print("3. Remove employee")
            print("press q to quit")

            action = input("Choose an option: ").lower()

            if action == "1":
                try:
                    remove_punct_map = dict.fromkeys(map(ord, string.punctuation))
                    name = input("Enter name: ").translate(remove_punct_map)
                    kt = input("Enter passport number: ").translate(remove_punct_map)
                    country = input("Enter country: ").translate(remove_punct_map)
                    address = input("Enter address: ").translate(remove_punct_map)
                    mail = input("Enter mail: ").strip()
                    phone = input("Enter phone number: ").translate(remove_punct_map)
                    customer_license = input("Enter drivers license: ").translate(remove_punct_map)
                    age = int(input("Enter age: "))
                    new_employee = Employee(name, kt, country, address, mail, phone, customer_license, age)
                    self.__employee_service.add_employee(new_employee)
                except Exception:
                    print("Check your inputs")

            elif action == '2':
                if len(self.__employee_service.get_employees()) == 0:
                    print("{}".format("No employees\n"))
                else:
                    emp = self.__employee_service.get_employees()
                    self.print_employees(emp)


            elif action == "3":
                try:
                    emp = self.__employee_service.get_employees()
                    self.print_employees(emp)
                    c_id = int(input("Select employee by Id: "))
                    emp = self.__employee_service.get_employee_by_id(c_id)
                    self.print_employees([emp])
                    self.__employee_service.remove_employee(c_id)
                    input("Press enter to continue")
                except Exception:
                    print("Something went wrong, please try again")


