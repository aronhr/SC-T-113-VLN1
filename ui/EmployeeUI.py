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

            elif action == "4":
                try:

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
                            employee.set_name(input("Enter new Name: ").translate(remove_punct_map))
                        elif choice == "2":
                            employee.set_kt(input("Enter new Passport: ").translate(remove_punct_map))
                        elif choice == "3":
                            employee.set_country(input("Enter new Country: ").translate(remove_punct_map))
                        elif choice == "4":
                            employee.set_address(input("Enter Address: ").translate(remove_punct_map))
                        elif choice == "5":
                            employee.set_mail(input("Enter new Mail: "))
                        elif choice == "6":
                            employee.set_phone_number(input("Enter new Phone number: ").translate(remove_punct_map))
                        elif choice == "7":
                            employee.set_license(input("Enter new License: ").translate(remove_punct_map))
                        elif choice == "8":
                            employee.set_age(input("Enter new Age: ").replace(string.punctuation, ""))

                    self.__employee_service.remove_employee(c_id)
                    self.__employee_service.add_employee(employee)
                    print(employee)
                    input("Press enter to continue")
                except Exception:
                    print("Something went wrong, please try again.")
