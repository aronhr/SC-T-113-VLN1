from repositories.CustomerRepository import Customer


class CustomerService:
    def __init__(self):
        self.__customer_repo = Customer()

    def add_customer(self, customer):
        self.__customer_repo.add_customer(customer)

    def get_customers(self):
        return self.__customer_repo.get_customer()

    def edit_customer(self, customer_id):
        return self.__customer_repo.edit_customer(customer_id)

    def remove_customer(self):
        pass


