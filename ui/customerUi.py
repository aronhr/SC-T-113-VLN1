from services.customerService import CustomerService
from modules.person.customer import Customer


class CustomerUi:

    def __init__(self):
        self.__customer_service = CustomerService()

    @staticmethod
    def print_header():
        print("{:^5}|{:^8}|{:^17}|{:^9}|{:^14}|{:^5}|{:^8}|{:^11}| {:^11}".format("ID", "Name", "Passport number",
                                                                                  "Country", "Phone number", "Age",
                                                                                  "Mail",
                                                                                  "Address", "Driver´s License"))

    def print_customer(self):
        print("-"*102)
        for ix, customer in enumerate(self.__customer_service.get_customers()):
            print("{:^5}{:^8}{:^17}{:^9}{:^14}{:^5}{:^8}{:^11} {:^11}".format(ix + 1, customer[0], customer[1],
                                                                              customer[2], customer[3],
                                                                              customer[4], customer[5],
                                                                              customer[6], customer[7]))

    def main_menu(self):
        action = ""
        while action != 'q':
            print("You can do the following: ")
            print("1. Add a customer")
            print("2. List all customers")
            print("press q to quit\n")

            action = input("Choose an option: ").lower()
            print()

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
                if len(self.__customer_service.get_customers()) == 0:
                    print("{}".format("No customers\n"))
                else:
                    self.print_header()
                    # customers_list = self.__customer_service.get_customers()
                    self.print_customer()
