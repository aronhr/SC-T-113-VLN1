"""
Það á að vera stór stafur í clasa!!
Þetta fer að verða pirrandi!
"""

from services.customerService import CustomerService
from modules.person.Customer import Customer
from services.OrderService import OrderService
from ui.OrdercarUi import OrdercarUi
import os
import string
remove_punct_map = dict.fromkeys(map(ord, string.punctuation))


class CustomerUi:

    def __init__(self):
        self.__customer_service = CustomerService()
        self.__order_service = OrderService()
        self.__orderUi = OrdercarUi()

    def print_customers(self):
        if self.__customer_service.get_customers() == "No customers":
            print("No customers")
        else:
            print("{:^6}|{:^18}|{:^17}|{:^11}|{:^17}|{:^22}|{:^14}|{:^18}|{:^5}|".format
                  ("ID", "Name", "Passport number", "Country", "Address", "E-mail", "Phone number", "Driver´s license", "Age"))
            print("-" * 137)
            for ix, customer in enumerate(self.__customer_service.get_customers()):
                print("{:^8}{:<19}{:<18}{:<12}{:<18}{:<23}{:<15}{:<19}{:<7}".format(ix + 1, customer["Name"], customer[
                    "Passport number"], customer["Country"], customer["Address"], customer["Mail"],
                     customer["Phone number"], customer["license"], customer["Age"]))
        print()

    def main_menu(self):
        action = ""
        while action != 'q':
            os.system('cls')
            print("Customers:")
            print("You can do the following: ")
            print("1. Add a customer")
            print("2. List all customers")
            print("3. List order history of customer")
            print("4. Edit customer")
            print("5. Delete customer")
            print("Press q to go back\n")

            action = input("Choose an option: ").lower()
            print()

            if action == "1":
                try:
                    print("Creating costumer:")
                    name = input("\tEnter name: ").translate(remove_punct_map)
                    kt = input("\tEnter passport number: ").translate(remove_punct_map)
                    country = input("\tEnter country: ").translate(remove_punct_map)
                    address = input("\tEnter address: ").translate(remove_punct_map)
                    mail = input("\tEnter mail: ").strip()
                    phone = input("\tEnter phone number: ").translate(remove_punct_map)
                    customer_license = input("\tEnter drivers license: ").translate(remove_punct_map)
                    age = int(input("\tEnter age: ").translate(remove_punct_map))
                    new_customer = Customer(name, kt, country, address, mail, phone, customer_license, age)
                    print(new_customer)
                    if input("Do you want create this costumer?(Y/N)").upper() == "Y":
                        self.__customer_service.add_customer(new_customer)
                        print("Customer created!")
                    else:
                        print("No costumer created.")
                except Exception:
                    print("Something went wrong, no costumer created.")
                input("Press enter to continue")

            elif action == "2":
                if len(self.__customer_service.get_customers()) == 0:
                    print("{}".format("No customers\n"))
                else:
                    self.print_customers()
                input("Press enter to continue")

            elif action == '3':
                kt = input("Enter passport number of the customer (q to go back): ").upper()
                if kt != "Q":
                    orders = self.__order_service.get_available_order_customer(kt)
                    self.__orderUi.print_completed_orders(orders)

            elif action == "4":
                if self.__customer_service.get_customers() != "No customers":
                    e_action = ''
                    self.print_customers()
                    customer_id = input("Chose which customer do you want to edit? (q to quit): ")
                    if customer_id.upper() == "Q":
                        continue
                    else:
                        customer_id = int(customer_id)
                        customer = self.__customer_service.get_customer_by_id(customer_id)
                        self.__customer_service.print_customer(customer_id)
                        new_customer = Customer(customer["Name"], customer["Passport number"], customer["Country"],
                                                customer["Address"],
                                                customer["Mail"], customer["Phone number"], customer["license"],
                                                customer["Age"])

                    while e_action != 'q':
                        print("\n1. Passport number/kt\n2. Name\n3. Country\n4. Address\n5. Phone number\n6. E-mail"
                              "\n7. Driver´s license\n8. Age\nq. Go back")

                        e_action = input("What to you want to edit?: ").lower()

                        if e_action == '1':
                            new_customer.set_kt(input("Enter passport number/kt: ").translate(remove_punct_map))
                        elif e_action == '2':
                            new_customer.set_name(input("Enter name: ").translate(remove_punct_map))
                        elif e_action == '3':
                            new_customer.set_country(input("Enter country: ").translate(remove_punct_map))
                        elif e_action == '4':
                            new_customer.set_address(input("Enter address: ").translate(remove_punct_map))
                        elif e_action == '5':
                            new_customer.set_phone_number(input("Enter phone number: ").translate(remove_punct_map))
                        elif e_action == '6':
                            new_customer.set_mail(input("Enter mail: ").strip())
                        elif e_action == '7':
                            new_customer.set_license(input("Enter driver´s license: ").translate(remove_punct_map))
                        elif e_action == '8':
                            new_customer.set_age(input("Enter age: ").translate(remove_punct_map))

                    self.__customer_service.add_customer(new_customer)
                    self.__customer_service.remove_customer(customer_id)
                else:
                    print("No customers to edit\n")
                input("Press enter to continue")

            elif action == "5":
                if self.__customer_service.get_customers() != "No customers":
                    self.print_customers()
                    customer_to_delete = input("What customer would you like to delete? (q to quit) ")
                    if customer_to_delete.upper() == "Q":
                        continue
                    else:
                        customer_to_delete = int(customer_to_delete)
                        self.__customer_service.remove_customer(customer_to_delete)
                else:
                    print("No customers to delete\n")
                input("Press enter to continue")
