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
            ("ID", "Name", "Passport number", "Country", "Address", "E-mail", "Phone number", "Driving license",
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
            kt = input("\tEnter Kt/passport number: ").translate(remove_punct_map)
            if self.__employee_service.check_kt(kt):
                print("\nCustomer already exists\n")
            else:
                name = input("\tEnter name: ").translate(remove_punct_map)
                country = input("\tEnter country: ").translate(remove_punct_map)
                address = input("\tEnter address: ").translate(remove_punct_map)
                mail = input("\tEnter mail: ").strip()
                phone = input("\tEnter phone number: ").translate(remove_punct_map)
                customer_license = int(input("\tEnter drivers license: "))
                age = int(input("\tEnter age: "))
                new_employee = Employee(name, kt, country, address, mail, phone, customer_license, age)
                print(new_employee)
                if input("Do you want to create this Employee? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").upper() == "Y":
                    self.__employee_service.add_employee(new_employee)
                    print("\nEmployee created!\n")
                else:
                    print("\nNo employee created.\n")

        except Exception:
            print("\n\33[;31mSomething went wrong, no employee created.\33[;0m\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def list_employees(self, employees):
        self.header("Employees")
        if employees:
            self.print_employees(employees)
        else:
            print("No employees\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def remove_employee(self, employees):
        self.header("Remove employee")
        if employees:
            removing = True
            while removing:
                self.print_employees(employees)
                employee_to_delete = input("Select employee by Id (\33[;31mq to quit\33[;0m): ")
                if employee_to_delete.isdigit():
                    try:
                        are_you_sure = input("Are you sure you want to delete this employee? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                        if are_you_sure == "y":
                            emp = self.__employee_service.get_employee_by_id(int(employee_to_delete))
                            self.print_employees([emp])
                            self.__employee_service.remove_employee(int(employee_to_delete))
                            removing = False
                    except Exception:
                        print("\n\33[;31mCanceled\33[;0m\n")
                elif employee_to_delete.lower() == 'q':
                    break
                else:
                    print("\nPlease enter a correct input\n")
        else:
            print("No employee to delete\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def edit_employee(self, employees):
        self.header("Edit employee")
        if employees:
            try:
                editing = True
                while editing:
                    self.print_employees(employees)
                    c_id = input("Select employee by Id (\33[;31mq to quit\33[;0m): ")
                    if c_id.isdigit() and int(c_id) <= len(employees):
                        employee = self.__employee_service.get_employee_by_id(int(c_id))
                        if employee:
                            self.print_employees([employee])
                            new_employee = Employee(employee["Name"], employee["Passport number"], employee["Country"],
                                                employee["Address"], employee["Mail"], employee["Phone number"],
                                                int(employee["license"]), employee["Age"])

                            choice = ""
                            while choice != "q":
                                print("\n1. Edit Name\n2. Edit Passport\n3. Edit country\n4. Edit Address\n5. Edit mail\n"
                                      "6. Edit Phone number\n7. Edit license\n8. Edit Age\n\n\33[;31mPress q to quit\33[;0m\n")
                                choice = input("Enter your choice: ").lower()
                                if choice == "1":
                                    new_employee.set_name(input("Enter new Name: ").translate(remove_punct_map))
                                elif choice == "2":
                                    new_employee.set_kt(input("Enter new Passport: ").translate(remove_punct_map))
                                elif choice == "3":
                                    new_employee.set_country(input("Enter new Country: ").translate(remove_punct_map))
                                elif choice == "4":
                                    new_employee.set_address(input("Enter Address: ").translate(remove_punct_map))
                                elif choice == "5":
                                    new_employee.set_mail(input("Enter new Mail: "))
                                elif choice == "6":
                                    new_employee.set_phone_number(input("Enter new Phone number: ").translate(remove_punct_map))
                                elif choice == "7":
                                    new_employee.set_license(input("Enter new License: ").translate(remove_punct_map))
                                elif choice == "8":
                                    new_employee.set_age(input("Enter new Age: ").replace(string.punctuation, ""))

                            self.__employee_service.remove_employee(int(c_id))
                            self.__employee_service.add_employee(new_employee)
                            print(new_employee)
                            editing = False
                    elif c_id.lower() == 'q':
                        break
                    else:
                        print("\n\33[;31mPlease enter a correct input\33[;0m\n")
            except Exception:
                print("\n\33[;31mSomething went wrong!\33[;0m\n")
        else:
            print("No employee to edit\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def main_menu(self):
        action = ""
        while action != 'q':
            employees = self.__employee_service.get_employees()
            os.system('cls')
            self.header("Employees")
            print("You can do the following: ")
            print("1. Add a employee\n2. List all employees\n3. Remove employee\n4. Edit employee\n\33[;31mPress q to go back \33[;0m")

            action = input("\nChoose an option: ").lower()

            if action == "1":
                self.add_employee()

            elif action == '2':
                self.list_employees(employees)

            elif action == "3":
                self.remove_employee(employees)

            elif action == "4":
                self.edit_employee(employees)
