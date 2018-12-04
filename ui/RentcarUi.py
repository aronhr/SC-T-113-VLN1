from services.CarService import CarService
from modules.car.Car import Car
from ui.CarUi import CarUi
from services.RentService import RentService
from modules.person.customer import Customer
from services.customerService import CustomerService
import string
import os


class RentcarUi:

    def __init__(self):
        self.__car_service = CarService()
        self.__car_ui = CarUi()
        self.__rent_service = RentService()
        self.__customer_service = CustomerService()

    def main_menu(self):
        os.system('cls')
        print("Rent car")
        kt = input("\tEnter Kt/Passport number: ")
        customer = self.__rent_service.check_kt(kt)
        if customer:
            print(customer)
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
        time = input("\tEnter time (dd-mm-yy dd-mm-yy)")
        cartype = input("\tEnter type of car: ")
        print("Available cars\n")
        cars_type = self.__car_service.get_cars_by_type(cartype)
        self.__car_ui.print_cars(cars_type)
        id = int(input("\tSelect car by Id: "))
        # TODO: IndexError: string index out of range
        # self.__car_ui.print_cars(cars_type[id])
        print(cars_type[id-1])
