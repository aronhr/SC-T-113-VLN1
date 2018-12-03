from ui.SalesmanUi import SalesmanUi
from ui.customerUi import CustomerUi


def main():
    ui = SalesmanUi()
    ui.main_menu()


def c_main():
    ui = CustomerUi()
    ui.main_menu()


c_main()
