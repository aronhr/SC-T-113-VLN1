from repositories.EmployeeRepository import EmployeeRepository


class EmployeeService:
    def __init__(self):
        self.__employee_repo = EmployeeRepository()

    def add_employee(self, customer):
        return self.__employee_repo.add_employee(customer)

    def get_employees(self):
        return self.__employee_repo.get_employee()
