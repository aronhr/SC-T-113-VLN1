from ui.CarUi import CarUi
from ui.customerUi import CustomerUi
from ui.OrdercarUi import OrdercarUi
from ui.EmployeeUI import EmployeeUI
import os
import ctypes


def open_fullscreen():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')

    SW_MAXIMIZE = 3

    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, SW_MAXIMIZE)


def car():
    print("\33[;95m")
    print("\t           __-------__")
    print("\t         / _---------_ \ ")
    print("\t        / /           \ \ ")
    print("\t        | |           | |")
    print("\t        |_|___________|_|")
    print("\t     /-\|               |/-\ ")
    print("\t    | _ |\      0      /| _ |")
    print("\t    |(_)| \     !     / |(_)|")
    print("\t    |___|__\____!____/__|___|")
    print("\t    [________|JABAN|________]")
    print("\t    ||||    ~~~~~~~~~    ||||")
    print("\t    `--'                 `--'")
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
    open_fullscreen()
    val = ""
    while val != "q":
        os.system('cls')
        car()
        print("-"*50)
        print("|{:^58}|".format("\33[95mQuick Fix Bílaleigan \33[;0m"))
        print("-"*50)
        print("Main menu\n1. Orders\n2. Customers\n3. Cars\n4. Employee\n\n""\33[;31mPress q to quit the program \33[;0m")

        val = input("\nChoose an option: ").lower()
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
