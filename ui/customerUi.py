from services.customerService import CustomerService
from modules.person.customer import Customer


class CustomerUi:

    def __init__(self):
        self.__customer_service = CustomerService()

    def main_menu(self):

        action = ""
        while action != 'q':
            print("You can do the following: ")
            print("1. Add a customer")
            print("2. List all customers")
            print("press q to quit")

            action = input("Choose an option: ").lower()

            if action == "1":
                name = input("Enter name: ")
                kt = input("Enter passport number: ")
                country = input("Enter country: ")
                address = input("Enter address: ")
                mail = input("Enter mail: ")
                phone = input("Enter phone number: ")
                customer_license = input("Enter drivers license: ")
                age = int(input("Enter age: "))
                new_customer = Customer(name, kt, country, address, mail, phone, customer_license, age)
                self.__customer_service.add_customer(new_customer)

            if action == '2':
                customers = self.__customer_service.get_customers()
                print(customers)