from ui.CarUi import CarUi
from ui.customerUi import CustomerUi
from ui.OrdercarUi import OrdercarUi
from ui.EmployeeUI import EmployeeUI
from repositories.OrderRepository import OrderRepository


def car_main():
    ui = CarUi()
    ui.main_menu()


def employee_main():
    ui = EmployeeUI()
    ui.main_menu()


def customer_main():
    ui = CustomerUi()
    ui.main_menu()


def order_main():
    ui = OrdercarUi()
    ui.main_menu()


def main():
    val = ""
    while val != "q":
        print("1. Orders\n2. Customers\n3. Cars\n4. Employee\nPress q to quit")
        val = input()
        if val == "1":
            order_main()
        elif val == "2":
            customer_main()
        elif val == "3":
            car_main()
        elif val == "4":
            employee_main()



main()
