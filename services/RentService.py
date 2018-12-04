from repositories.RentRepository import RentRepository
from repositories.CustomerRepository import CustomerRepository


class RentService:
    def __init__(self):
        self.__rent_repo = RentRepository()
        self.__customer_repo = CustomerRepository()

    def check_kt(self, kt):
        return self.__customer_repo.check_if_kt_exist(kt)

    def add_rent(self, rent):
        if self.is_valid_rent(rent):
            self.__rent_repo.add_rent(rent)

    def is_valid_rent(self, rent):
        # here should be some code to
        # validate the car
        return True

    def get_rent(self):
        return self.__rent_repo.get_rent()

    def get_rent_by_type(self, genre):
        pass

    def get_available_rent(self):
        return self.__rent_repo.get_available_rent("True")

    def get_not_available_rent(self):
        return self.__rent_repo.get_available_rent("False")

    def get_rent_by_id(self, id):
        return self.__rent_repo.get_rent_id(id)
