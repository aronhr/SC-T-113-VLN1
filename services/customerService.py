from repositories.CustomerRepository import CustomerRepository


class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def get_customers(self):
        return self.__customer_repo.get_customer()

    def edit_customer(self, customer_id, action):
        pass
       # return self.__customer_repo.edit_customer(customer_id, action)

    def remove_customer(self, customer_id):
        return self.__customer_repo.remove_customer(customer_id)

    def get_customer_by_id(self, c_id):
        return self.__customer_repo.get_customer_id(c_id - 1)

    def print_customer(self, c_id):
        return self.__customer_repo.print_customer(c_id)

