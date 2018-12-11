from services.CarService import CarService
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

    @staticmethod
    def print_current_orders(orders):
        if len(orders) == 0:
            print("No orders\n")
        else:
            print("{:^6}|{:^12}|{:^20}|{:^17}|{:^21}|{:^21}|{:^12}|{:^11}|{:^13}|{:^6}".format
                  ("ID", "Kt", "Name", "Car-license", "From date", "To date", "Price", "Insurance", "Total price", "Days"))
            print("-" * 149)
            for ix, order in enumerate(orders):
                print("{:^8} {:^12} {:<20} {:<19} {:<24} {:<18} {:<12} {:<11} {:<13} {:<6}".format
                      (ix + 1, order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                       order["Price"], order["Insurance"], order["Total price"], order["Days"]))

    @staticmethod
    def print_completed_orders(completed_orders):
        if len(completed_orders) == 0:
            print("No orders")
        else:
            print("{:^6}|{:^12}|{:^20}|{:^17}|{:^21}|{:^21}|{:^20}|{:^21}|{:^11}|{:^13}|{:^6}".format
                  ("ID", "Kt", "Name", "License", "From date", "To date", "Price", "Payment method", "Insurance",
                   "Total price", "Days"))

            print("-" * 180)
            for ix, order in enumerate(completed_orders):
                print("{:^6}  {:<12}  {:<20}  {:<17}  {:<21}  {:<21}  {:<20}  {:<21} {:<11} {:<13} {:<6}".format
                      (ix + 1, order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                       order["Price"], order["Payment method"], order["Insurance"], order["Total price"], order["Days"]))

    def print_receipt(self, order):
        car = self.__car_service.get_car_by_license(order["License"])
        customer = self.__customer_service.get_customer_by_kt(order["Kt"])

        receipt = """
                            Customer
                                Kt/Passport number: {i}
                                              Name: {name} 
                                            E-Mail: {mail}
                                      Phone number: {phone} 
                                   Driving license: {license} 
                                               Age: {age}
                                           Country: {country} 
                                           Address: {address}

                            Car                                      Days
                                    License plate: {car_license}
                                            Model: {car_model}
                                             Type: {car_type}
                                            Class: {car_class}
                                            Seats: {car_seats}
                                              4x4: {car_fwd}
                                     Transmission: {car_transmission}
                                     Price of car: {car_price}                  {order_days}
                                        Insurance: {order_insurance}                   {order_days}
                                      Total price: ------------------------------------ {order_price} kr.

                                        """
        output = receipt.format(i=customer["Passport number"], name=customer["Name"], mail=customer["Mail"],
                                address=customer["Address"], country=customer["Country"],
                                license=customer["license"],
                                age=customer["Age"], phone=customer["Phone number"], car_license=car["License"],
                                car_model=car["Model"], car_type=car["Type"], car_class=car["Class"],
                                car_seats=car["Seats"], car_fwd=car["4x4"], car_transmission=car["Transmission"],
                                car_price=car["Price"], price=order["Price"], order_insurance=order["Insurance"],
                                order_days=order["Days"], order_price=order["Total price"])

        print(output)

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
        print("-" * 50)
        print("|{:^48}|".format("Rent car"))
        print("-" * 50)
        kt = input("\tEnter Kt/Passport number: ").translate(remove_punct_map)
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
            age = int(input("\tEnter age: "))
            new_customer = Customer(name, kt, country, address, mail, phone, customer_license, age)
            self.__customer_service.add_customer(new_customer)

        approved = False
        while not approved:
            from_date = self.__car_service.user_date("\tEnter start date for rent (dd/mm/yy): ")
            to_date = self.__car_service.user_date("\tEnter end date for rent (dd/mm/yy): ")
            for x in self.__car_service.get_car_class():
                print(str(x), end=' ')
            print()
            car_type = input("\tEnter type of car (q to quit): ").translate(remove_punct_map)
            if car_type.upper() == "Q":
                break
            print("Available cars\n")

            available_cars_type = self.__car_service.get_available_date_type(car_type, from_date, to_date)

            if len(available_cars_type) == 0:
                i = input("No cars available,(Press q to quit, enter to select another date)")
                if i == "q":
                    break
            else:
                while not approved:
                    self.__car_ui.print_cars(available_cars_type)
                    try:
                        c_id = input("\nSelect car by Id (q to quit): ").upper()
                        if c_id == "Q":
                            approved = True
                            break
                        c_id = int(c_id)
                        self.__car_ui.print_cars([available_cars_type[c_id - 1]])

                        chosen_car_plate = available_cars_type[c_id - 1]["License"]
                        price_of_order = int(available_cars_type[c_id - 1]["Price"])

                        # Calculate how long the order is in days
                        from_date = datetime.datetime.date(from_date)
                        to_date = datetime.datetime.date(to_date)
                        delta = to_date - from_date
                        days = delta.days   # how many days the rental is

                        price_of_order_days = price_of_order * days     # Price for car multiplied with days
                        print("Price of order: {} ISK".format(price_of_order_days))
                        insurance = input("Would you like extra insurance for {} ISK per day? Y/N: ".format(
                            int(price_of_order) * 0.75)).upper()    # Insurance (Yes or No)
                        price_of_order_days_insurance = price_of_order_days
                        if insurance == 'Y':
                            price_of_order_days_insurance = price_of_order_days * 1.75  # Price of order with extra insurance
                            print("Price of order: {} ISK".format(price_of_order_days_insurance))
                            deposit = price_of_order_days_insurance * 0.10
                            print("Your deposit of the order is {} ISK".format(deposit))
                        else:
                            deposit = price_of_order_days * 0.10
                            print("Your deposit of the order is {} ISK".format(deposit))

                        book = input("Order car? Y/N: ").upper()
                        if book == 'Y':
                            if customer:
                                name = customer["Name"]

                            new_order = Order(kt, name, chosen_car_plate, from_date, to_date, price_of_order_days,
                                              insurance, price_of_order_days_insurance, days)
                            self.__order_service.add_order(new_order, False)
                            print("\nOrder successful!\n")
                            approved = True
                        else:
                            continue
                    except IndexError:
                        print("ID not available")

    def return_car(self):
        try:
            orders = self.__order_service.get_orders()
            if len(orders) == 0:
                print("\nNo orders")
            else:
                self.print_current_orders(orders)
                o_id = input("Select order by Id: ")
                order = self.__order_service.get_order_by_id(int(o_id))
                self.print_current_orders([order])
                price = float(order["Total price"])
                km_length = int(input("Enter the km driven: "))
                days = order["Days"]
                max_km = 100 * int(days)
                if km_length > max_km:
                    for x in range(km_length - max_km):
                        price *= 1.01
                print(price)
                self.print_receipt(order)
                self.__order_service.pay_order(round(price), order)
                self.__order_service.remove_order(int(o_id))
                print("Car Returned!")
        except Exception as e:
            print("Something went wrong, please try again", e)

    def revoke_order(self):
        try:
            orders = self.__order_service.get_orders()
            if len(orders) == 0:
                print("\nNo orders")
            else:
                self.print_current_orders(orders)
                o_id = int(input("Select order by Id (q to quit): "))
                order = self.__order_service.get_order_by_id(o_id)
                self.print_current_orders([order])
                print("Your deposit was {} ISK".format(order["Price"] * 0.10))
                self.__order_service.remove_order(o_id)
                print("Order revoked and deposit returned")

        except Exception:
            print("Canceled")

    def edit_current_order(self):
        orders = self.__order_service.get_orders()
        self.print_current_orders(orders)
        o_id = int(input("Select order by Id: "))
        order = self.__order_service.get_order_by_id(o_id)
        edited_order = Order(order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                             order["Price"], order["Insurance"], order["Total price"], order["Days"])
        a_choice = ''
        while a_choice != 'q':
            a_choice = input(
                "1. Edit name\n2. License\n3. From date\n4. To date\n5. Price\nPress q to go back").lower()
            if a_choice == '1':
                edited_order.set_renter(input("Enter new name: ").translate(remove_punct_map))
            elif a_choice == '2':
                edited_order.set_car(input("Enter new license: ").translate(remove_punct_map))
            elif a_choice == '3':
                edited_order.set_from_date(
                    datetime.datetime.strftime(self.__car_service.user_date("Enter new from date: "), "%d/%m/%y"))
            elif a_choice == '4':
                edited_order.set_to_date(
                    datetime.datetime.strftime(self.__car_service.user_date("Enter new to date: "), "%d/%m/%y"))
            elif a_choice == '5':
                edited_order.set_price(input("Enter new price: ").translate(remove_punct_map))
        print(edited_order)
        self.__order_service.remove_order(o_id)
        self.__order_service.add_order(edited_order, True)

    def edit_completed_order(self):
        orders = self.__order_service.get_completed_orders()
        self.print_completed_orders(orders)
        o_id = int(input("Select order by Id: "))
        order = self.__order_service.get_order_by_id(o_id)
        edited_order = Order(order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                             order["Price"], order["Insurance"], order["Total price"], order["Days"], order["Payment method"])
        b_choice = ''
        while b_choice != 'q':
            b_choice = input(
                "What do you want to order?\n1. Name\n2. License\n3. From Date\n4. To date\n5. Price\n6. "
                "Payment "
                "method\n Press q to go back").lower()
            if b_choice == '1':
                edited_order.set_renter(input("Enter new name: ").translate(remove_punct_map))
            elif b_choice == '2':
                edited_order.set_car(input("Enter new license: ").translate(remove_punct_map))
            elif b_choice == '3':
                edited_order.set_from_date(
                    datetime.datetime.strftime(self.__car_service.user_date("Enter new from date: "), "%d/%m/%y"))
            elif b_choice == '4':
                edited_order.set_to_date(
                    datetime.datetime.strftime(self.__car_service.user_date("Enter new to date: "), "%d/%m/%y"))
            elif b_choice == '5':
                edited_order.set_price(input("Enter new price: ").translate(remove_punct_map))
            elif b_choice == '6':
                edited_order.set_payment_method(input("Enter new payment method: ").translate(remove_punct_map))
        self.__order_service.remove_order(o_id)
        self.__order_service.add_order(edited_order, True)
        input("Press enter to continue")

    def main_menu(self):
        action = ''
        while action != 'q':
            os.system('cls')
            print("Orders:")
            print("You can do the following: ")
            print("1. Rent a car")
            print("2. Return car")
            print("3. Current orders")
            print("4. Completed orders")
            print("5. Revoke order")
            print("6. Edit order")
            print("7. List order history of car")
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
                self.print_current_orders(orders)
                input("Press enter to continue")

            elif action == '4':
                completed_orders = self.__order_service.get_completed_orders()
                self.print_completed_orders(completed_orders)
                o_id = input("Select the order you want to view (q to quit): ")
                if o_id == "q":
                    break
                os.system('cls')
                order = self.__order_service.get_completed_order_id(int(o_id))
                self.print_receipt(order)

                input("Press enter to continue")

            elif action == '5':
                self.revoke_order()
                input("Press enter to continue")

            elif action == '6':
                print("1. Edit current orders\n2. Edit completed orders\nq to quit")
                e_action = input().upper()
                if action != "Q":
                    if e_action == '1':
                        self.edit_current_order()
                    elif e_action == '2':
                        self.edit_completed_order()

            elif action == "7":
                license = input("Enter car license plate (q to quit): ").upper()
                if license != "Q":
                    orders = self.__order_service.get_available_orders(license)
                    self.print_completed_orders(orders)
                input("Press enter to continue")
