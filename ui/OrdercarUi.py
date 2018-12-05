from services.CarService import CarService
from modules.car.Car import Car
from ui.CarUi import CarUi
from services.OrderService import OrderService
from modules.person.Customer import Customer
from services.customerService import CustomerService
from repositories.CustomerRepository import CustomerRepository
import datetime
import string
import os


class OrdercarUi:
    def __init__(self):
        self.__car_service = CarService()
        self.__car_ui = CarUi()
        self.__rent_service = OrderService()
        self.__customer_service = CustomerService()
        self.__customer_repo = CustomerRepository()

    def print_customer(self, customer):
        print("\tPassport number: {}".format(customer["Passport number"]))
        print("\tName: {}".format(customer["Name"]))
        print("\tCountry: {}".format(customer["Country"]))
        print("\tAddress: {}".format(customer["Address"]))
        print("\tPhone number: {}".format(customer["Phone number"]))
        print("\tE-mail: {}".format(customer["Mail"]))
        print("\tDriver´s license: {}".format(customer["license"]))
        print("\tAge: {}".format(customer["Age"]))

    def main_menu(self):
        os.system('cls')
        print("Rent car")
        kt = input("\tEnter Kt/Passport number: ")
        customer = self.__rent_service.check_kt(kt)
        if customer:
            self.print_customer(customer)
        else:
            name = input("\tEnter name: ")
            country = input("\tEnter country: ")
            address = input("\tEnter address: ")
            mail = input("\tEnter mail: ")
            phone = input("\tEnter phone number: ")
            customer_license = input("\tEnter drivers license: ")
            age = int(input("\tEnter age: "))
            new_customer = Customer(name, kt, country, address, mail, phone, customer_license, age)
            self.__customer_service.add_customer(new_customer)

        from_date = self.__car_service.user_date("\tEnter start date for rent (dd/mm/yy): ")
        to_date = self.__car_service.user_date("\tEnter end date for rent (dd/mm/yy): ")

        cartype = input("\tEnter type of car: ")
        print("Available cars\n")

        available_cars_type = self.__car_service.get_available_date_type(cartype, from_date, to_date)
        self.__car_ui.print_cars(available_cars_type)

        c_id = int(input("\tSelect car by Id: "))
        self.__car_ui.print_cars([available_cars_type[c_id-1]])

        chosen_car = available_cars_type[c_id - 1]["Numberplate"]
        print(chosen_car)

        