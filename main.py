from ui.CarUi import CarUi
from ui.customerUi import CustomerUi
from ui.RentcarUi import RentcarUi
from ui.EmployeeUI import EmployeeUI



def car_main():
    ui = CarUi()
    ui.main_menu()

def employee_main():
    ui = EmployeeUI()
    ui.main_menu()


def customer_main():
    ui = CustomerUi()
    ui.main_menu()


def rent_main():
    ui = RentcarUi()
    ui.main_menu()


def main():

    val = ""
    while val != "q":
        print("1. Rent car\n2. Return car\n3. Customers\n4. Orders\n5. Cars\n6. Employee\nPress q to quit")
        val = input()
        if val == "1":
            rent_main()
        elif val == "2":
            pass
        elif val == "3":
            customer_main()
        elif val == "4":
            pass
        elif val == "5":
            car_main()
        elif val == "6":
            employee_main()
        elif val == "q":
            exit(0)


main()
