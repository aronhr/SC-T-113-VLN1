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

    def header(self, i):
        print("-" * 50)
        print("|{:^48}|".format(i))
        print("-" * 50)
        print()

    # noinspection PyTypeChecker
    def print_customer(self, customer):
        print("\nPassport number: {}".format(customer["Passport number"]))
        print("Name: {}".format(customer["Name"]))
        print("Country: {}".format(customer["Country"]))
        print("Address: {}".format(customer["Address"]))
        print("Phone number: {}".format(customer["Phone number"]))
        print("E-mail: {}".format(customer["Mail"]))
        print("Driver´s license: {}".format(customer["license"]))
        print("Age: {}".format(customer["Age"]))
        print("-" * 35)

    @staticmethod
    def print_customers(customers):
        print("{:^6}|{:^18}|{:^17}|{:^11}|{:^17}|{:^30}|{:^14}|{:^18}|{:^5}|".format
              ("ID", "Name", "Passport number", "Country", "Address", "E-mail", "Phone number", "Driving license", "Age"))
        print("-" * 145)
        for ix, customer in enumerate(customers):
            print("{:^8}{:<19}{:<18}{:<12}{:<18}{:<31}{:<15}{:<19}{:<7}".format(ix + 1, customer["Name"], customer[
                "Passport number"], customer["Country"], customer["Address"], customer["Mail"],
                 customer["Phone number"], customer["license"], customer["Age"]))
        print()

    def add_customer(self):
        self.header("Add customer")
        try:
            print("Creating customer:")
            kt = input("\tEnter kt/passport number: ").translate(remove_punct_map)
            if self.__order_service.check_kt(kt):
                print("\nCustomer already exists!\n")
            elif not self.__order_service.check_kt(kt):
                name = input("\tEnter name: ").translate(remove_punct_map)
                country = input("\tEnter country: ").translate(remove_punct_map)
                address = input("\tEnter address: ").translate(remove_punct_map)
                mail = input("\tEnter mail: ").strip()
                phone = input("\tEnter phone number: ").translate(remove_punct_map)
                customer_license = input("\tEnter driving license: ").translate(remove_punct_map)
                age = int(input("\tEnter age: ").translate(remove_punct_map))
                new_customer = Customer(name, kt, country, address, mail, phone, customer_license, age)
                print(new_customer)
                if input("Do you want create this customer? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").upper() == "Y":
                    self.__customer_service.add_customer(new_customer)
                    print("\nCustomer created!\n")
            else:
                print("\nNo customer created.\n")
        except Exception:
            print("\n\33[;31mSomething went wrong, please try again!\33[;0m\n")
        input("\33[;32mPress enter to continue\33[;0m")

    def list_all_customers(self):
        self.header("All customers")
        customers = self.__customer_service.get_customers()
        if customers:
            self.print_customers(customers)
        else:
            print("\nNo customers\n")
        input("\33[;32mPress enter to continue\33[;0m")

    def edit_customer(self):
        self.header("Edit customer")
        customers = self.__customer_service.get_customers()
        if customers:
            e_action = ''
            self.print_customers(customers)
            customer_id = input("Which customer do you want to edit? (\33[;31mq to quit\33[;0m): ").lower()
            if customer_id != "q":
                try:
                    customer_id = int(customer_id)

                    customer = self.__customer_service.get_customer_by_id(customer_id)
                    self.print_customer(customer)
                    new_customer = Customer(customer["Name"], customer["Passport number"], customer["Country"],
                                            customer["Address"],
                                            customer["Mail"], customer["Phone number"], customer["license"],
                                            customer["Age"])

                    while e_action != 'q':
                        print("\n1. Passport number/kt.\n2. Name\n3. Country\n4. Address\n5. Phone number"
                              "\n6. E-mail\n7. Driving license\n8. Age\n\33[;31mPress q to go back\33[;0m")

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
                            new_customer.set_license(input("Enter driving license: ").translate(remove_punct_map))
                        elif e_action == '8':
                            new_customer.set_age(input("Enter age: ").translate(remove_punct_map))

                    self.__customer_service.add_customer(new_customer)
                    self.__customer_service.remove_customer(customer_id)
                except Exception:
                    print("\n\33[;31mWrong input, try again!\33[;0m\n")
        else:
            print("\nNo customers to edit\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def remove_customer(self):
        self.header("Remove customer")
        customers = self.__customer_service.get_customers()
        if customers:
            self.print_customers(customers)
            customer_to_delete = input("What customer would you like to remove? (\33[;31mq to quit\33[;0m): ").lower()
            if customer_to_delete != "q":
                try:
                    are_you_sure = input("Are you sure you want to remove this customer? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if are_you_sure == "y":
                        customer_to_delete = int(customer_to_delete)
                        print("\nCustomer number {} removed\n".format(customer_to_delete))
                        self.__customer_service.remove_customer(customer_to_delete)

                except Exception:
                    print("\n\33[;31mWrong input, try again!\33[;0m")
        else:
            print("\n\33[;31mNo customers to delete!\33[;0m\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def see_customer(self):
        self.header("See customer")
        kt = input("Enter kt/passport number of the customer(\33[;31mq to go back\33[;0m): ").upper()
        customer = self.__order_service.check_kt(kt)
        if customer:
            self.print_customer(customer)
        elif not customer:
            print("\nCustomer does not exist\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def main_menu(self):
        action = ""
        while action != 'q':
            os.system('cls')
            self.header("Customer")
            print("You can do the following: \n1. Add a customer\n2. List all customers\n3. Edit customer"
                  "\n4. Remove customer\n5. See customer\n\n""\33[;31mPress q to go back\33[;0m")
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

            elif action == "5":
                self.see_customer()
