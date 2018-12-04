from repositories.CustomerRepository import CustomerRepository


class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def get_customers(self):
        return self.__customer_repo.get_customer()


