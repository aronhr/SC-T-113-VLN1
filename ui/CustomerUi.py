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

    @staticmethod
    def print_customers(customers):
        print("{:^6}|{:^18}|{:^17}|{:^11}|{:^17}|{:^30}|{:^14}|{:^18}|{:^5}|".format
              ("ID", "Name", "Passport number", "Country", "Address", "E-mail", "Phone number", "Driver´s license", "Age"))
        print("-" * 137)
        for ix, customer in enumerate(customers):
            print("{:^8}{:<19}{:<18}{:<12}{:<18}{:<31}{:<15}{:<19}{:<7}".format(ix + 1, customer["Name"], customer[
                "Passport number"], customer["Country"], customer["Address"], customer["Mail"],
                 customer["Phone number"], customer["license"], customer["Age"]))
        print()

    def add_customer(self):
        try:
            print("Creating customer:")
            name = input("\tEnter name: ").translate(remove_punct_map)
            kt = input("\tEnter kt/passport number: ").translate(remove_punct_map)
            country = input("\tEnter country: ").translate(remove_punct_map)
            address = input("\tEnter address: ").translate(remove_punct_map)
            mail = input("\tEnter mail: ").strip()
            phone = input("\tEnter phone number: ").translate(remove_punct_map)
            customer_license = input("\tEnter drivers license: ").translate(remove_punct_map)
            age = int(input("\tEnter age: ").translate(remove_punct_map))
            new_customer = Customer(name, kt, country, address, mail, phone, customer_license, age)
            print(new_customer)
            if input("Do you want create this customer? (Y/N)").upper() == "Y":
                self.__customer_service.add_customer(new_customer)
                print("\nCustomer created!\n")
            else:
                print("\nNo customer created.\n")
        except Exception:
            print("\nSomething went wrong, no customer created.\n")
        input("Press enter to continue")

    def list_all_customers(self):
        customers = self.__customer_service.get_customers()
        if customers:
            self.print_customers(customers)
        else:
            print("\nNo customers\n")
        input("Press enter to continue")

    def edit_customer(self):
        customers = self.__customer_service.get_customers()
        if customers:
            e_action = ''
            self.print_customers(customers)
            customer_id = input("Chose which customer do you want to edit? (q to quit): ").lower()
            if customer_id != "q":
                try:
                    customer_id = int(customer_id)

                    customer = self.__customer_service.get_customer_by_id(customer_id)
                    self.__customer_service.print_customer(customer_id)
                    new_customer = Customer(customer["Name"], customer["Passport number"], customer["Country"],
                                            customer["Address"],
                                            customer["Mail"], customer["Phone number"], customer["license"],
                                            customer["Age"])

                    while e_action != 'q':
                        print("\n1. Passport number/kt\n2. Name\n3. Country\n4. Address\n5. Phone number"
                              "\n6. E-mail\n7. Driver´s license\n8. Age\nq. Go back")

                        e_action = input("Choose an option: ").lower()

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
                except Exception:
                    print("\nWrong input, try again!\n")
        else:
            print("\nNo customers to edit\n")
        input("Press enter to continue")

    def remove_customer(self):
        customers = self.__customer_service.get_customers()
        if customers:
            self.print_customers(customers)
            customer_to_delete = input("What customer would you like to remove? (q to quit) ").lower()
            if customer_to_delete != "q":
                try:
                    are_you_sure = input("Are you sure you want to delete this customer? (Y/N) ").lower()
                    if are_you_sure == "y":
                        customer_to_delete = int(customer_to_delete)
                        print("\ncustomer number {} deleted\n".format(customer_to_delete))
                        self.__customer_service.remove_customer(customer_to_delete)

                except Exception:
                    print("\nWrong input, try again!\n")
        else:
            print("\nNo customers to delete\n")
        input("Press enter to continue")

    def main_menu(self):
        action = ""
        while action != 'q':
            os.system('cls')
            print("Customers:")
            print("You can do the following: \n1. Add a customer\n2. List all customers\n3. Edit customer"
                  "\n4. Remove customer\n\n""\33[;31mPress q to go back \33[;0m")
            action = input("\nChoose an option: ").lower()
            print()
            if action == "1":
                self.add_customer()

            elif action == "2":
                self.list_all_customers()

            elif action == "3":
                self.edit_customer()

            elif action == "4":
                self.remove_customer()
