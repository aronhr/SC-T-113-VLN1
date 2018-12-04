from services.customerService import CustomerService
from modules.person.customer import Customer
import os
import string


class CustomerUi:

    def __init__(self):
        self.__customer_service = CustomerService()

    def print_customers(self):
        print("{:^5}|{:^8}|{:^17}|{:^11}|{:^9}|{:^17}|{:^14}|{:^18}|{:^5}|".format("ID", "Name", "Passport number",
                                                                                   "Country", "Address", "E-mail",
                                                                                   "Phone number", "Driver´s license",
                                                                                   "Age"))
        print("-" * 112)
        for ix, customer in enumerate(self.__customer_service.get_customers()):
            print("{:<7}{:<10}{:<18}{:<11}{:<10}{:<18}{:<15}{:<19}{:<7}".format(ix + 1, customer["Name"], customer[
                "Passport number"], customer["Country"], customer["Address"], customer["Mail"],
                                                                                customer["Phone number"],
                                                                                customer["license"], customer["Age"]))
        print()

    def main_menu(self):
        action = ""
        while action != 'q':
            os.system('cls')
            print("You can do the following: ")
            print("1. Add a customer")
            print("2. List all customers")
            print("3. Edit customer")
            print("4. Delete customer")
            print("press q to quit\n")

            action = input("Choose an option: ").lower()
            print()

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
                    new_customer = Customer(name, kt, country, phone, age, mail, address, customer_license)
                    self.__customer_service.add_customer(new_customer)
                except Exception:
                    print("Hlep")

            elif action == "2":
                if len(self.__customer_service.get_customers()) == 0:
                    print("{}".format("No customers\n"))
                else:
                    self.print_customers()

            elif action == "3":
                self.print_customers()
                customer_id = int(input("Chose which customer do you want to edit?: "))
                self.__customer_service.edit_customer(customer_id)

            elif action == "4":
                pass
