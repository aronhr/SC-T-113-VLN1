from repositories.EmployeeRepository import EmployeeRepository


class EmployeeService:
    def __init__(self):
        self.__employee_repo = EmployeeRepository()

    def add_employee(self, customer):
        return self.__employee_repo.add_employee(customer)

    def get_employees(self):
        return self.__employee_repo.get_employee()

    def get_employee_by_id(self, id):
        return self.__employee_repo.get_employee_id(id - 1)

    def remove_employee(self, id):
        return self.__employee_repo.remove_employee_id(id)

    def check_kt(self, kt):
        return self.__employee_repo.check_if_kt_exist(kt)
