from ui.CarUi import CarUi
from ui.customerUi import CustomerUi
from ui.OrdercarUi import OrdercarUi
from ui.EmployeeUI import EmployeeUI
import os


def car():
    print("\33[;34m")
    print("\t\t\t        __-------__")
    print("\t\t\t      / _---------_ \ ")
    print("\t\t\t     / /           \ \ ")
    print("\t\t\t     | |           | |")
    print("\t\t\t     |_|___________|_|")
    print("\t\t\t  /-\|               |/-\ ")
    print("\t\t\t | _ |\      0      /| _ |")
    print("\t\t\t |(_)| \     !     / |(_)|")
    print("\t\t\t |___|__\____!____/__|___|")
    print("\t\t\t [________|JABAN|________]")
    print("\t\t\t ||||    ~~~~~~~~~    ||||")
    print("\t\t\t `--'                 `--'")
    print("\33[;0m")


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
        os.system('cls')
        car()
        print("-"*50)
        print("|{:^48}|".format("Bílaleiga Guðfinns"))
        print("-"*50)
        print("Main menu\n1. Orders\n2. Customers\n3. Cars\n4. Employee\nPress q to quit\n")
        val = input("Choose an option: ").lower()
        print()
        if val == "1":
            order_main()
        elif val == "2":
            customer_main()
        elif val == "3":
            car_main()
        elif val == "4":
            employee_main()


main()
