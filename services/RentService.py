from repositories.RentRepository import RentRepository
from repositories.CustomerRepository import CustomerRepository


class RentService:
    def __init__(self):
        self.__rent_repo = RentRepository()
        self.__customer_repo = CustomerRepository()

    def check_kt(self, kt):
        return self.__customer_repo.check_if_kt_exist(kt)