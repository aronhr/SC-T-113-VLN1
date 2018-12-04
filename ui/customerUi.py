from services.customerService import CustomerService
from modules.person.customer import Customer
import os
import string


class CustomerUi:

    def __init__(self):
        self.__customer_service = CustomerService()

    def print_customers(self):
        if self.__customer_service.get_customers() == "No customers":
            print("No customers")
        else:
            print(
                "{:^6}|{:^12}|{:^17}|{:^11}|{:^17}|{:^22}|{:^14}|{:^18}|{:^5}|".format("ID", "Name", "Passport number",
                                                                                       "Country", "Address", "E-mail",
                                                                                       "Phone number",
                                                                                       "Driver´s license",
                                                                                       "Age"))
            print("-" * 131)
            for ix, customer in enumerate(self.__customer_service.get_customers()):
                print("{:^8}{:<13}{:<18}{:<12}{:<18}{:<23}{:<15}{:<19}{:<7}".format(ix + 1, customer["Name"], customer[
                    "Passport number"], customer["Country"], customer["Address"], customer["Mail"],
                                                                                    customer["Phone number"],
                                                                                    customer["license"],
                                                                                    customer["Age"]))
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
                    new_customer = Customer(name, kt, country, address, mail, phone, customer_license, age)
                    self.__customer_service.add_customer(new_customer)
                except Exception:
                    print("Hlep")

            elif action == "2":
                if len(self.__customer_service.get_customers()) == 0:
                    print("{}".format("No customers\n"))
                else:
                    self.print_customers()

            elif action == "3":
                e_action = ''
                self.print_customers()
                customer_id = int(input("Chose which customer do you want to edit?: "))
                customer = self.__customer_service.get_customer_by_id(customer_id)
                self.__customer_service.print_customer(customer_id)
                new_customer = Customer(customer["Name"], customer["Passport number"], customer["Country"],
                                        customer["Address"],
                                        customer["Mail"], customer["Phone number"], customer["license"],
                                        customer["Age"])

                while e_action != 'q':
                    print("\n1. Passport number/kt\n2. Name\n3. Country\n4. Address\n5. Phone number\n6. E-mail"
                          "\n7. Driver´s license\n8. Age\nq. Go back")

                    e_action = input("What to you want to edit: ?").lower()

                    if e_action == '1':
                        new_customer.set_kt(input("Enter passport number/kt: "))
                    elif e_action == '2':
                        new_customer.set_name(input("Enter name: "))
                    elif e_action == '3':
                        new_customer.set_country(input("Enter country: "))
                    elif e_action == '4':
                        new_customer.set_address(input("Enter address: "))
                    elif e_action == '5':
                        new_customer.set_phone_number(input("Enter phone number: "))
                    elif e_action == '6':
                        new_customer.set_mail(input("Enter mail: "))
                    elif e_action == '7':
                        new_customer.set_license(input("Enter driver´s license: "))
                    elif e_action == '8':
                        new_customer.set_age(input("Enter age: "))

                self.__customer_service.add_customer(new_customer)
                self.__customer_service.remove_customer(customer_id)

            elif action == "4":
                self.print_customers()
                customer_to_delete = int(input("What customer would you like to delete? "))
                self.__customer_service.remove_customer(customer_to_delete)
