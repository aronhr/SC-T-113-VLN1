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
            print("4. Edit employee ")
            print("press q to quit")

            action = input("Choose an option: ").lower()

            if action == "1":
                try:
                    name = input("Enter name: ").replace(string.punctuation, "")
                    kt = input("Enter passport number: ").replace(string.punctuation, "")
                    country = input("Enter country: ").replace(string.punctuation, "")
                    address = input("Enter address: ").replace(string.punctuation, "")
                    mail = input("Enter mail: ").replace(string.punctuation, "")
                    phone = input("Enter phone number: ").replace(string.punctuation, "")
                    customer_license = input("Enter drivers license: ").replace(string.punctuation, "")
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

            elif action == "4":

                employee = self.__employee_service.get_employees()
                self.print_employees(employee)
                c_id = int(input("Select employee by Id: "))
                employee = self.__employee_service.get_employee_by_id(c_id)
                self.print_employees([employee])
                employee = Employee(employee["Name"], employee["Passport number"], employee["Country"], employee["Address"], employee["Mail"], employee["Phone number"],
                          int(employee["license"]), employee["Age"])

                choice = ""
                while choice != "q":
                    print("\n1. Edit Name\n2. Edit Passport\n3. Edit country\n4. Edit Address\n5. Edit mail\n"
                          "6. Edit Phone number\n7. Edit license\n8. Edit Age\npress q to quit")
                    choice = input("Enter your choice: ").lower()
                    if choice == "1":
                        employee.set_name(input("Enter new Name: ").replace(string.punctuation, ""))
                    elif choice == "2":
                        employee.set_kt(input("Enter new Passport: ").replace(string.punctuation, ""))
                    elif choice == "3":
                        employee.set_country(input("Enter new Country: ").replace(string.punctuation, ""))
                    elif choice == "4":
                        employee.set_address(input("Enter Address: ").replace(string.punctuation, ""))
                    elif choice == "5":
                        employee.set_mail(input("Enter new Mail: ").upper().replace(string.punctuation, ""))
                    elif choice == "6":
                        employee.set_phone_number(input("Enter new Phone number: ").upper().replace(string.punctuation, ""))
                    elif choice == "7":
                        employee.set_license(input("Enter new License: ").upper().replace(string.punctuation, ""))
                    elif choice == "8":
                        employee.set_age(
                            input("Enter new Age: ").upper().replace(string.punctuation, ""))

                self.__employee_service.remove_employee(c_id)
                self.__employee_service.add_employee(employee)
                print(employee)
                input("Press enter to continue")


