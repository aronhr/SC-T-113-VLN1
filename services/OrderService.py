from repositories.OrderRepository import OrderRepository
from repositories.CustomerRepository import CustomerRepository


class OrderService:
    def __init__(self):
        self.__order_repo = OrderRepository()
        self.__customer_repo = CustomerRepository()

    def check_kt(self, kt):
        return self.__customer_repo.check_if_kt_exist(kt)

    def add_order(self, new_order, edit):
        return self.__order_repo.add_order(new_order, edit)

    def get_orders(self):
        return self.__order_repo.get_orders()

    def get_order_by_id(self, o_id):
        return self.__order_repo.get_order_id(o_id - 1)

    def get_completed_order_id(self, o_id):
        return self.__order_repo.get_completed_order_id(o_id - 1)

    def remove_order(self, o_id):
        return self.__order_repo.remove_order_id(o_id)

    def pay_order(self, price, order):
        return self.__order_repo.pay_order(price, order)

    def get_completed_orders(self):
        return self.__order_repo.get_completed_orders()

    def get_available_orders(self, license):
        orders = self.__order_repo.get_completed_orders()
        if orders:
            order = []
            for x in orders:
                if x["License"] == license:
                    order.append(x)
            return order
        else:
            return False

    def get_available_order_customer(self, kt):
        """
        Gets available order by "kt"
        :param kt:
        :return:
        """
        orders = self.__order_repo.get_completed_orders()
        if orders:
            order = []
            for x in orders:
                if x["Kt"] == kt:
                    order.append(x)
            return order
        else:
            return False
