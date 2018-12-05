from repositories.OrderRepository import OrderRepository
from repositories.CustomerRepository import CustomerRepository


class OrderService:
    def __init__(self):
        self.__rent_repo = OrderRepository()
        self.__customer_repo = CustomerRepository()

    def check_kt(self, kt):
        return self.__customer_repo.check_if_kt_exist(kt)