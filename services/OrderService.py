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

    def get_order_by_id(self, o_id):
        return self.__order_repo.get_order_id(o_id - 1)

    def remove_order(self, o_id):
        return self.__order_repo.remove_order_id(o_id)
