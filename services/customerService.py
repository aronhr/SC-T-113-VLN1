from repositories.CustomerRepository import CustomerRepository


class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    @staticmethod
    def print_customers(customers):
        print("{:^6}|{:^18}|{:^17}|{:^11}|{:^17}|{:^30}|{:^14}|{:^18}|{:^5}|".format
              ("ID", "Name", "Passport number", "Country", "Address", "E-mail", "Phone number", "Driving license",
               "Age"))
        print("-" * 145)
        for ix, customer in enumerate(customers):
            print("{:^8}{:<19}{:<18}{:<12}{:<18}{:<31}{:<15}{:<19}{:<7}".format(ix + 1, customer["Name"], customer[
                "Passport number"], customer["Country"], customer["Address"], customer["Mail"],
                                                                                customer["Phone number"],
                                                                                customer["license"], customer["Age"]))
        print()

    def list_all_customers(self):
        customers = self.get_customers()
        if customers:
            self.print_customers(customers)
        else:
            print("No customers\n")

    # noinspection PyTypeChecker
    @staticmethod
    def print_customer(customer):
        print("\tPPN/Kt: {}".format(customer["Passport number"]))
        print("\tName: {}".format(customer["Name"]))
        print("\tCountry: {}".format(customer["Country"]))
        print("\tAddress: {}".format(customer["Address"]))
        print("\tPhone number: {}".format(customer["Phone number"]))
        print("\tE-mail: {}".format(customer["Mail"]))
        print("\tDriver´s license: {}".format(customer["license"]))
        print("\tAge: {}".format(customer["Age"]))


    def add_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def get_customers(self):
        return self.__customer_repo.get_customer()

    def get_customer_by_kt(self, kt):
        customers = self.get_customers()
        for x in customers:
            if x["Passport number"] == kt:
                return x
        return 0

    def remove_customer(self, customer_id):
        return self.__customer_repo.remove_customer(customer_id)

    def get_customer_by_id(self, c_id):
        return self.__customer_repo.get_customer_id(c_id - 1)
