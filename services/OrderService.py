from repositories.OrderRepository import OrderRepository
from repositories.CustomerRepository import CustomerRepository


class OrderService:
    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__customer_repo = CustomerRepository()

    def check_kt(self, kt):
        return self.__customer_repo.check_if_kt_exist(kt)

    def add_order(self, new_order):
        return self.__order_repo.add_order(new_order)

    def get_orders(self):
        return self.__order_repo.get_orders()