from services.EmployeeService import EmployeeService
from modules.person.Employee import Employee
import string

class EmployeeUI:
    def __init__(self):
        self.__employee_service = EmployeeService()

    def main_menu(self):

        action = ""
        while action != 'q':
            print("You can do the following: ")
            print("1. Add a employee")
            print("2. List all employees")
            print("press q to quit")

            action = input("Choose an option: ").lower()
#4
            if action == "1":
                kt = input("Enter kt: ")
                fname = input("Enter first name: ").replace(string.punctuation, "")
                lname = input("Enter last name: ").replace(string.punctuation, "")
                email = input("Enter mail: ")
                phone = input("Enter phone number: ")
                new_employee = Employee(kt, fname, lname, email, phone)
                self.__employee_service.add_employee(new_employee)

            if action == '2':
                employee = self.__employee_service.get_employees()
                print(employee)
