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
    def header(i):
        """
        This is the header on the user interface. we user this format in the functions down below
        :param i:
        :return:
        """
        print("-" * 50)
        print("|{:^48}|".format(i))
        print("-" * 50)
        print()

    def add_customer(self):
        """
        Adds an customer by asking the customer for a few details
        :return:
        """
        self.header("Add customer")
        con = True
        while con:
            try:
                kt = input("\tEnter PPN/Kt (\33[;31mq to go back\33[;0m): ").lower().translate(remove_punct_map)
                if self.__order_service.check_kt(kt):
                    print("\nCustomer already exists!\n")
                elif kt =="q":
                    break
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
        """
        List all of the customers
        :return:
        """
        self.header("All customers")
        self.__customer_service.list_all_customers()
        input("\33[;32mPress enter to continue\33[;0m")

    def edit_customer(self):
        """
        Offer you to edit an customer by id.
        :return:
        """
        self.header("Edit customer")
        customers = self.__customer_service.get_customers()
        if customers:
            editing_customer = True
            while editing_customer:
                e_action = ''
                self.__customer_service.print_customers(customers)
                customer_id = input("Which customer do you want to edit?(\33[;31mq to quit\33[;0m): ").lower()
                if customer_id.isdigit() and int(customer_id) <= len(customers):
                    try:
                        customer_id = int(customer_id)

                        customer = self.__customer_service.get_customer_by_id(customer_id)
                        self.__customer_service.print_customer(customer)
                        new_customer = Customer(customer["Name"], customer["Passport number"], customer["Country"],
                                                customer["Address"],
                                                customer["Mail"], customer["Phone number"], customer["license"],
                                                customer["Age"])

                        while e_action != 'q':
                            print("\n1. Passport number/kt.\n2. Name\n3. Country\n4. Address\n5. Phone number"
                                  "\n6. E-mail\n7. Driving license\n8. Age\n\n\33[;31mPress q to go back\33[;0m\n")

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

                        self.__customer_service.remove_customer(customer_id)
                        self.__customer_service.add_customer(new_customer)
                        print("\nCustomer edited\n")
                        editing_customer = False
                        break
                    except Exception:
                        print("\n\33[;31mWrong input, try again!\33[;0m\n")
                        print("\n\33[;31mWrong input, try again!\33[;0m\n")
                else:
                    print("\n\33[;31mWrong input, try again!\33[;0m\n")
        else:
            print("No customers to edit\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def remove_customer(self):
        """
        Remove a specific customer, removes the content in the csv file and appears it without the removed customer
        :return:
        """
        self.header("Remove customer")
        customers = self.__customer_service.get_customers()
        if customers:
            removing_customer = True
            while removing_customer:
                self.__customer_service.print_customers(customers)
                customer_to_delete = input("What customer would you like to remove? (\33[;31mq to quit\33[;0m): ").lower()
                if customer_to_delete.isdigit() and int(customer_to_delete) <= len(customers) + 1:
                    try:
                        are_you_sure = input("Are you sure you want to remove this customer? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                        if are_you_sure == "y":
                            customer_to_delete = int(customer_to_delete)
                            print("\nCustomer number {} removed\n".format(customer_to_delete))
                            self.__customer_service.remove_customer(customer_to_delete)
                            removing_customer = False
                    except Exception:
                        print("\n\33[;31mWrong input, try again!\33[;0m")
                elif customer_to_delete.lower() == 'q':
                    removing_customer = False
                    break
                else:
                    print("\n\33[;31mWrong input, try again!\33[;0m\n")
        else:
            print("\33[;31mNo customers to delete!\33[;0m\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def see_customer(self):
        """
        offers you to see a specific customer with "PPN/kt"
        :return:
        """
        self.header("See customer")
        kt = input("Enter PPN/Kt of the customer(\33[;31mq to go back\33[;0m): ").upper()
        customer = self.__order_service.check_kt(kt)
        if customer:
            self.__customer_service.print_customer(customer)
        elif not customer:
            print("\nCustomer does not exist\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def main_menu(self):
        """
        This is the main menu for the customer user interface. you can (e. add customer)
        :return:
        """
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
