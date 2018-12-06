from services.CarService import CarService
from modules.car.Car import Car
from ui.CarUi import CarUi
from services.OrderService import OrderService
from modules.person.Customer import Customer
from services.customerService import CustomerService
from repositories.CustomerRepository import CustomerRepository
from modules.order.order import Order
import datetime
import os
import string
remove_punct_map = dict.fromkeys(map(ord, string.punctuation))


class OrdercarUi:
    def __init__(self):
        self.__car_service = CarService()
        self.__car_ui = CarUi()
        self.__order_service = OrderService()
        self.__customer_service = CustomerService()
        self.__customer_repo = CustomerRepository()

    def print_orders(self, orders):
        if self.__order_service.get_orders() == "No orders":
            print("No orders")
        else:
            print(
                "{:^6}|{:^12}|{:^17}|{:^21}|{:^21}".format("ID", "Name", "Car-license", "From date", "To date"))

            print("-" * 82)

            for ix, order in enumerate(orders):
                print("{:^6}{:^12}{:^19}{:^24}{:^18}".format(ix + 1, order["Name"], order["License"], order["From date"], order["To date"]))

    @staticmethod
    def print_customer(customer):
        print("\tPassport number: {}".format(customer["Passport number"]))
        print("\tName: {}".format(customer["Name"]))
        print("\tCountry: {}".format(customer["Country"]))
        print("\tAddress: {}".format(customer["Address"]))
        print("\tPhone number: {}".format(customer["Phone number"]))
        print("\tE-mail: {}".format(customer["Mail"]))
        print("\tDriver´s license: {}".format(customer["license"]))
        print("\tAge: {}".format(customer["Age"]))

    def rent_car(self):
        print("Rent car")
        kt = input("\tEnter Kt/Passport number: ")
        customer = self.__order_service.check_kt(kt)
        if customer:
            self.print_customer(customer)
        else:
            name = input("\tEnter name: ").translate(remove_punct_map)
            country = input("\tEnter country: ").translate(remove_punct_map)
            address = input("\tEnter address: ").translate(remove_punct_map)
            mail = input("\tEnter mail: ").strip()
            phone = input("\tEnter phone number: ").translate(remove_punct_map)
            customer_license = input("\tEnter drivers license: ").translate(remove_punct_map)
            age = int(input("\tEnter age: ")).translate(remove_punct_map)
            new_customer = Customer(name, kt, country, address, mail, phone, customer_license, age)
            self.__customer_service.add_customer(new_customer)
        approved = False

        while not approved:

            from_date = self.__car_service.user_date("\tEnter start date for rent (dd/mm/yy): ")
            to_date = self.__car_service.user_date("\tEnter end date for rent (dd/mm/yy): ")

            cartype = input("\tEnter type of car: ").translate(remove_punct_map)
            print("Available cars\n")

            available_cars_type = self.__car_service.get_available_date_type(cartype, from_date, to_date)
            if len(available_cars_type) == 0:
                i = input("No cars available,(Press q to quit, enter to select another date)")
                if i == "q":
                    break
            else:
                self.__car_ui.print_cars(available_cars_type)

                c_id = int(input("\nSelect car by Id: "))
                self.__car_ui.print_cars([available_cars_type[c_id - 1]])
                chosen_car_plate = available_cars_type[c_id - 1]["License"]

                try:
                    new_order = Order(customer["Name"], chosen_car_plate, from_date, to_date)
                    self.__order_service.add_order(new_order)
                    print("Order successful!")
                    approved = True
                except Exception as e:
                    print(e)

    def return_car(self):
        try:
            orders = self.__order_service.get_orders()
            self.print_orders(orders)
            o_id = int(input("Select order by Id: "))
            order = self.__order_service.get_order_by_id(o_id)
            self.print_orders([order])
            self.__order_service.remove_order(o_id)
            print("Car Returned!")
            input("Press enter to continue")
        except Exception as e:
            # print("Something went wrong, please try again")
            print(e)

    def main_menu(self):
        action = ''
        while action != 'q':
            os.system('cls')
            print("Orders:")
            print("You can do the following: ")
            print("1. Rent a car")
            print("2. Return car")
            print("3. All orders")
            print("Press q to quit")

            action = input()
            if action == '1':
                self.rent_car()
                input("Press enter to continue")
            elif action == '2':
                self.return_car()
                input("Press enter to continue")
            elif action == '3':
                orders = self.__order_service.get_orders()
                self.print_orders(orders)
                input("Press enter to continue")
