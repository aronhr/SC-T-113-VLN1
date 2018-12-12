from services.EmployeeService import EmployeeService
from modules.person.Employee import Employee
import string
import os

remove_punct_map = dict.fromkeys(map(ord, string.punctuation))


class EmployeeUI:
    def __init__(self):
        self.__employee_service = EmployeeService()

    def header(self, i):
        print("-" * 50)
        print("|{:^48}|".format(i))
        print("-" * 50)
        print()

    @staticmethod
    def print_employees(emp):
        print(
            "{:^6}|{:^18}|{:^17}|{:^11}|{:^17}|{:^22}|{:^14}|{:^18}|{:^5}|".format
            ("ID", "Name", "Passport number", "Country", "Address", "E-mail", "Phone number", "Driver´s license",
             "Age"))
        print("-" * 137)
        for ix, customer in enumerate(emp):
            print("{:^8}{:<19}{:<18}{:<12}{:<18}{:<23}{:<15}{:<19}{:<7}".format
                  (ix + 1, customer["Name"], customer["Passport number"], customer["Country"], customer["Address"],
                   customer["Mail"], customer["Phone number"], customer["license"], customer["Age"]))
        print()

    def add_employee(self):
        self.header("Add employee")
        try:
            print("Creating Employee:")
            name = input("\tEnter name: ").translate(remove_punct_map)
            kt = input("\tEnter passport number: ").translate(remove_punct_map)
            country = input("\tEnter country: ").translate(remove_punct_map)
            address = input("\tEnter address: ").translate(remove_punct_map)
            mail = input("\tEnter mail: ").strip()
            phone = input("\tEnter phone number: ").translate(remove_punct_map)
            customer_license = int(input("\tEnter drivers license: "))
            age = int(input("\tEnter age: "))
            new_employee = Employee(name, kt, country, address, mail, phone, customer_license, age)
            print(new_employee)
            if input("Do you want to create this Employee? (Y/N) ").upper() == "Y":
                self.__employee_service.add_employee(new_employee)
                print("\nEmployee created!\n")
            else:
                print("\nNo employee created.\n")
        except Exception:
            print("\nSomething went wrong, no employee created.\n")
        input("Press enter to continue")

    def list_employees(self, employees):
        self.header("Employees")
        if employees:
            self.print_employees(employees)
        else:
            print("\nNo employees\n")
        input("Press enter to continue")

    def remove_employee(self, employees):
        self.header("Remove employee")
        if employees:
            self.print_employees(employees)
            employee_to_delete = int(input("Select employee by Id (q to quit): "))
            if employee_to_delete != "q":
                try:
                    are_you_sure = input("Are you sure you want to delete this employee? (Y/N) ").lower()
                    if are_you_sure == "y":
                        emp = self.__employee_service.get_employee_by_id(employee_to_delete)
                        self.print_employees([emp])
                        self.__employee_service.remove_employee(employee_to_delete)
                except Exception:
                    print("\nCanceled\n")
        else:
            print("\nNo employee to delete\n")
        input("Press enter to continue")

    def edit_employee(self, employees):
        self.header("Edit employee")
        if employees:
            try:
                self.print_employees(employees)
                c_id = int(input("Select employee by Id (q to quit): "))

                employee = self.__employee_service.get_employee_by_id(c_id)
                self.print_employees([employee])
                employee = Employee(employee["Name"], employee["Passport number"], employee["Country"],
                                    employee["Address"], employee["Mail"], employee["Phone number"],
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
            except Exception:
                print("\nSomething went wrong!\n")
        else:
            print("\nNo employee to edit\n")
        input("Press enter to continue")

    def main_menu(self):
        action = ""
        while action != 'q':
            employees = self.__employee_service.get_employees()
            os.system('cls')
            self.header("Employees")
            print("You can do the following: ")
            print(
                "1. Add a employee\n2. List all employees\n3. Remove employee\n4. Edit employee\n\n""\33[;31mPress q to go back \33[;0m")

            action = input("\nChoose an option: ").lower()

            if action == "1":
                self.add_employee()

            elif action == '2':
                self.list_employees(employees)

            elif action == "3":
                self.remove_employee(employees)

            elif action == "4":
                self.edit_employee(employees)
