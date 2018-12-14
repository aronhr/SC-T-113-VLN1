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
import math

remove_punct_map = dict.fromkeys(map(ord, string.punctuation))


class OrdercarUi:
    def __init__(self):
        self.__car_service = CarService()
        self.__car_ui = CarUi()
        self.__order_service = OrderService()
        self.__customer_service = CustomerService()
        self.__customer_repo = CustomerRepository()

    def header(self, i):
        print("-" * 50)
        print("|{:^48}|".format(i))
        print("-" * 50)
        print()

    def print_receipt(self, order):
        """
        Prints out the receipt for a customer and shows a few details (e. price)
        :param order:
        :return:
        """
        car = self.__car_service.get_car_by_license(order["License"])
        customer = self.__customer_service.get_customer_by_kt(order["Kt"])

        receipt = """
Customer

                PPN/Kt: {i:<30}
                  Name: {name:<30}
                E-Mail: {mail:<30}
          Phone number: {phone:<30}
       Driving license: {license:<30}
                   Age: {age:<30}
               Country: {country:<30}
               Address: {address:<30}
                                                                From day: {from_day:<8}
                                                                  To day: {to_day:<8}

     Car                                |     Per day     |   Quantity   |     Total
  -----------------------------------------------------------------------------------

         License plate: {car_license:<20}
                 Model: {car_model:<20}
                  Type: {car_type:<20}
                 Class: {car_class:<20}
                 Seats: {car_seats:<20}
                   4x4: {car_fwd:<20}
          Transmission: {car_transmission:<20}
          Price of car: {car_price:<20}{car_price:>6} kr.{order_days:^20}{car_order_price:>7} kr.
             Insurance: {order_insurance:<20}{insurance_price:>6} kr.{order_days:^20}{insurance_order_price:>7} kr.
               Penalty: {order_penalty:>57} kr.

           Total price: ------------------------------------------------- {order_price} kr.

                                        """
        if order["Insurance"] == "No":
            i_price = 0
            t_price = 0
        else:
            i_price = int(car["Price"]) * 0.25
            t_price = (int(car["Price"]) * 0.25) * int(order["Days"])

        output = receipt.format(i=customer["Passport number"], name=customer["Name"], mail=customer["Mail"],
                                address=customer["Address"], country=customer["Country"],
                                license=customer["license"],
                                age=customer["Age"], phone=customer["Phone number"], car_license=car["License"],
                                car_model=car["Model"], car_type=car["Type"], car_class=car["Class"],
                                car_seats=car["Seats"], car_fwd=car["4x4"], car_transmission=car["Transmission"],
                                car_price=car["Price"], price=order["Price"], order_insurance=order["Insurance"],
                                order_days=order["Days"], order_price=order["Total price"],
                                car_order_price=(int(car["Price"]) * int(order["Days"])),
                                insurance_order_price=round(t_price),
                                insurance_price=round(i_price), from_day=order["From date"], to_day=order["To date"],
                                order_penalty=round(float(order["Penalty"])))
        print(output)

    @staticmethod
    def calculate_days(from_date, to_date):
        """
        Calulates how many days the customer have used the car. from and to
        :param from_date:
        :param to_date:
        :return:
        """
        # Calculate how long the order is in days
        from_date = datetime.datetime.date(from_date)
        to_date = datetime.datetime.date(to_date)
        delta = to_date - from_date
        return delta.days  # how many days the rental is

    def create_customer(self, kt):
        """
        This asks you for information about customer (e. Enter country)

        :param kt:
        :return:
        """
        name = input("\tEnter name: ").translate(remove_punct_map)
        country = input("\tEnter country: ").translate(remove_punct_map)
        address = input("\tEnter address: ").translate(remove_punct_map)
        mail = input("\tEnter mail: ").strip()
        phone = input("\tEnter phone number: ").translate(remove_punct_map)
        customer_license = input("\tEnter drivers license: ").translate(remove_punct_map)
        age = int(input("\tEnter age: "))
        new_customer = Customer(name, kt, country, address, mail, phone, customer_license, age)
        self.__customer_service.add_customer(new_customer)
        return name

    def print_car_types(self):
        """
        Prints out the type of the car, we user the get car class to help us with this function
        :return:
        """
        cars = self.__car_service.get_car_class()
        if cars:
            print("\n\t", end="")
            for x in cars:
                print(str(x), end=' ')
            print()
            return True
        else:
            return False

    def rent_car(self):
        """
        This rents a car and ask the customer for a few details.
        :return:
        """
        self.header("Rent car")
        con = True
        while con:
            # self.__customer_service.list_all_customers()
            kt = input("Enter PPN/Kt(\33[;31mq to go back\33[;0m): ").lower().translate(remove_punct_map)
            if kt == "q":
                break
            elif input("Select this PPN/Kt(\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").format(kt).lower() == "y":
                con = False
                customer = self.__order_service.check_kt(kt)

                if customer:
                    self.__customer_service.print_customer(customer)
                else:
                    name = self.create_customer(kt)

                approved = False
                while not approved:
                    from_date = self.__car_service.user_date("Enter start date for rent (dd/mm/yy): ")

                    is_valid = False
                    while not is_valid:

                        to_date = self.__car_service.user_date("Enter end date for rent (dd/mm/yy): ")

                        if from_date <= to_date:
                            is_valid = True

                        else:
                            print("Time traveling?")

                    car_type = self.__car_service.check_car_class("Enter class: \n\t\33[;36m1. Luxury\n\t2. Sport\n\t"
                                                                  "3. Off-road\n\t4. Sedan\n\t5. Economy\33[;0m\n"
                                                                  "Select class: ", "Invalid input")
                    available_cars_type = self.__car_service.get_available_date_type(car_type, from_date, to_date)

                    if not available_cars_type:
                        i = input("No cars available,(\33[;31mpress q to quit\33[;0m,\33[;32m"
                                  " enter to select another date\33[;0m)")
                        if i == "q":
                            break
                    if car_type and available_cars_type:
                        while not approved:
                            print("\nAvailable cars\n")
                            c_id = self.__car_ui.print_cars(available_cars_type)
                            if c_id.lower() == 'q':
                                print("\nCanceled, please select another date\n")
                                break
                            try:
                                if c_id.isdigit():
                                    c_id = int(c_id)
                                    selected_car = available_cars_type[c_id - 1]
                                    chosen_car_plate = selected_car["License"]
                                    price_of_order = int(selected_car["Price"])

                                    print("\nSelected car: {}\n".format(chosen_car_plate))

                                    days = self.calculate_days(from_date, to_date)
                                    if days == 0:
                                        days = 1
                                    price_of_order_days = price_of_order * days     # Price for car multiplied with days

                                    print("Price of order: {} ISK".format(int(price_of_order_days)))
                                    insurance = input("Would you like extra insurance for {} {}".format  # Insurance (Yes or No)
                                                      (int(price_of_order * 0.25), "ISK per day? (\33[;32mY\33[;0m/"
                                                                                   "\33[;31mN\33[;0m): ")).upper()
                                    price_of_order_days_insurance = price_of_order_days

                                    if insurance == 'Y':
                                        price_of_order_days_insurance = price_of_order_days * 1.25  # Price of order with extra insurance
                                        print("Price of order: {} ISK".format(int(price_of_order_days_insurance)))
                                        deposit = price_of_order_days_insurance * 0.10
                                    else:
                                        deposit = price_of_order_days * 0.10

                                    print("Your deposit of the order is {} ISK".format(int(deposit)))

                                    book = input("Order car? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").upper()
                                    if book == 'Y':
                                        if customer:
                                            name = customer["Name"]

                                        new_order = Order(kt, name, chosen_car_plate, from_date, to_date,
                                                          price_of_order_days, insurance, price_of_order_days_insurance, days)
                                        self.__order_service.add_order(new_order, False)
                                        print("\nOrder successful!\n")
                                        approved = True
                                    else:
                                        print("\nOrder canceled!\n")
                                else:
                                    print("\nPlease enter correct input")
                            except IndexError:
                                print("ID not available")
                input("\33[;32mPress enter to continue \33[;0m")

    def return_car(self):
        """
        Here will the car be returned.
        :return:
        """
        self.header("Return car")
        returning = True
        correct_km = True
        while returning:
            try:
                orders = self.__order_service.get_orders()
                if orders:
                    self.__order_service.print_current_orders(orders)
                    o_id = input("Select order by Id (\33[;31mq to go back\33[;0m): ")
                    if o_id.isdigit():
                        order = self.__order_service.get_order_by_id(int(o_id))
                        current_order = Order(order["Kt"], order["Name"], order["License"], order["From date"],
                                              order["To date"], order["Price"], order["Insurance"],
                                              order["Total price"], order["Days"])
                        print(current_order)
                        price = float(order["Total price"])
                        while correct_km:
                            current_order.set_penalty(0)
                            km_length = input("Enter the km driven: ")
                            if km_length.isdigit():
                                max_km = 100 * int(order["Days"])
                                penalty = 0
                                if int(km_length) > max_km:
                                    for x in range(int(km_length) - max_km):
                                        penalty += int(order["Price"]) / int(order["Days"]) * 0.01
                                current_order.set_price_insurance(price+penalty)
                                current_order.set_penalty(penalty)
                                self.__order_service.remove_order(o_id)
                                self.__order_service.add_order(current_order, True)
                                order = self.__order_service.get_order_by_id(int(o_id))
                                self.print_receipt(order)
                                if self.__order_service.pay_order(round(price), order):
                                    self.__order_service.remove_order(int(o_id))
                                    print("\nCar Returned!\n")
                                    input("\33[;32mPress enter to continue \33[;0m")
                                    returning = False
                                    correct_km = False
                                else:
                                    print("\nCar payment not accepted!\n")
                                break
                            else:
                                print("\nPlease enter a correct input\n")

                    elif o_id.lower() == 'q':
                        print("\nReturning order canceled\n")
                        input("\33[;32mPress enter to continue\33[;0m")
                        break
                    else:
                        print("\nPlease enter a correct input\n")
                else:
                    print("No cars in rent\n")
                    input("\33[;32mPress enter to continue \33[;0m")
                    break

            except Exception:
                print("\nPlease enter a correct input\n")

    def revoke_order(self):
        """
        Here the order will be revoked.
        :return:
        """
        self.header("Revoke order")
        try:
            orders = self.__order_service.get_orders()
            if orders:
                revoking = True
                while revoking:
                    self.__order_service.print_current_orders(orders)
                    o_id = input("Select order by Id (\33[;31mq to quit\33[;0m""): ")
                    if o_id.isdigit():
                        order = self.__order_service.get_order_by_id(int(o_id))
                        if order:
                            print("Name: {} License of car: {} Total Price: {}".format(order["Name"], order["License"],
                                                                                       order["Total price"]))
                            total_price = float(order["Total price"])
                            print("Your deposit was {} ISK".format(int(total_price * 0.10)))
                            choice = input("Are you sure you want to revoke the order? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                            if choice == 'y':
                                self.__order_service.remove_order(o_id)
                                print("\nOrder revoked and deposit returned\n")
                                revoking = False
                                break
                            else:
                                print("\nRevoke canceled\n")
                                revoking = False
                        else:
                            print("\n\33[;31mWrong input try again\33[;0m\n")
                    if o_id.lower() == 'q':
                        break
                    else:
                        print("\n\33[;31mWrong input try again\33[;0m\n")
            else:
                print("\nNo orders\n")
        except Exception:
            print("\nRevoke failed\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def edit_current_order(self):
        """
        Here you cant edit a specific order by id (e. edit name)
        :return:
        """
        self.header("Edit order")
        orders = self.__order_service.get_orders()
        editing_order = True
        while editing_order:
            if orders:
                self.__order_service.print_current_orders(orders)
                o_id = input("Select order by Id (\33[;31mq to quit\33[;0m""): ")
                if o_id.lower() == 'q':
                    editing_order = False
                    break
                if o_id.isdigit():
                    order = self.__order_service.get_order_by_id(int(o_id))
                    if order:
                        edited_order = Order(order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                                             order["Price"], order["Insurance"], order["Total price"], order["Days"])
                        a_choice = ''
                        while a_choice != 'q':
                            print("1. Edit PPN/Kt\n2. Edit name\n3. Car-license\n4. From date\n5. To date\n6. Price\n7. Insurance\n"
                                  "8. Days\n\n""\33[;31mPress q to go back \33[;0m\n")
                            a_choice = input("Choose an option: ").lower()
                            if a_choice.lower() == 'q':
                                break
                            elif a_choice == "1":
                                edited_order.set_kt(input("Enter new Kt: ").translate(remove_punct_map))
                            elif a_choice == '2':
                                edited_order.set_renter(input("Enter new name: ").translate(remove_punct_map))
                            elif a_choice == '3':
                                edited_order.set_car(input("Enter new license: ").translate(remove_punct_map))
                            elif a_choice == '4':
                                edited_order.set_from_date(
                                    datetime.datetime.strftime(self.__car_service.user_date("Enter new from date: "), "%d/%m/%y"))
                            elif a_choice == '5':
                                edited_order.set_to_date(
                                    datetime.datetime.strftime(self.__car_service.user_date("Enter new to date: "), "%d/%m/%y"))
                            elif a_choice == '6':
                                edited_order.set_price(input("Enter new price: ").translate(remove_punct_map))
                            elif a_choice == '7':
                                edited_order.set_insurance(input("Enter new insurance \33[;32mY\33[;0m/\33[;31mN\33"
                                                                 "[;0m: ").translate(remove_punct_map))
                            elif a_choice == '8':
                                edited_order.set_days(input("Enter number of days: ").translate(remove_punct_map))
                            else:
                                print("\n\33[;31mWrong input try again\33[;0m\n")
                        self.__order_service.remove_order(o_id)
                        self.__order_service.add_order(edited_order, True)
                        print("\nOrder edited\n")
                        editing_order = False
                    else:
                        print("\n\33[;31mWrong input try again\33[;0m\n")
                else:
                    print("\n\33[;31mWrong input try again\33[;0m\n")
            else:
                print("No orders to edit\n")
                input("\33[;32mPress enter to continue \33[;0m")
                break
        input("\33[;32mPress enter to continue \33[;0m")

    def get_order_history_of_customer(self):
        """
        Gets order history of customer. and messages you if you have no orders
        :return:
        """
        self.header("Order history of customer")
        history = True
        while history:
            kt = input("Enter PPN/Kt of the customer(\33[;31mq to go back\33[;0m): ").upper()
            orders = self.__order_service.get_available_order_customer(kt)
            check_kt = self.__order_service.check_kt(kt)
            if kt == 'Q':
                history = False
            elif check_kt and orders:
                self.__order_service.print_completed_orders(orders)
                history = False
            elif not check_kt:
                print("\nCustomer does not exist\n")
            elif not orders:
                print("\nCustomer has no orders\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def history_of_car(self):
        self.header("Order history of car")
        history = True
        while history:
            cars = self.__car_service.get_cars()

            car_id = self.__car_ui.print_cars(cars)
            if car_id.isdigit():
                car = self.__car_service.get_car_by_id(int(car_id))
                car_orders = self.__order_service.get_available_orders(car["License"])
                if car and car_orders:
                    self.__order_service.print_completed_orders(car_orders)
                    history = False
                elif not car:
                    print("\nCar does not exist\n")
                elif not car_orders:
                    print("\nThe car has not been rented\n")
                    history = False
            elif car_id.lower() == 'q':
                break
        input("\33[;32mPress enter to continue \33[;0m")

    def completed_orders(self):
        """
        Here you can find a specific completed order
        :return:
        """
        self.header("Completed orders")
        try:
            completed_orders = self.__order_service.get_completed_orders()
            correct_id = True
            while correct_id:
                if completed_orders:
                    self.__order_service.print_completed_orders(completed_orders)
                    o_id = input("Select the order you want to view (\33[;31mq to go back\33[;0m): ")
                    if o_id.isdigit():
                        os.system('cls')
                        order = self.__order_service.get_completed_order_id(int(o_id))
                        self.print_receipt(order)
                        correct_id = False
                    elif o_id.lower() == 'q':
                        correct_id = False
                        break
                    else:
                        print("\nPlease enter a correct input\n")
                else:
                    print("No orders are complete\n")
                    correct_id = False
        except Exception:
            print("Something went wrong")
        input("\33[;32mPress enter to continue\33[;0m")

    def main_menu(self):
        """
        This is the main menu for the Order car interface, this will offer you to choose (e. 1. Rent a car)
        
        :return:
        """
        action = ''
        while action != 'q':
            os.system('cls')
            self.header("Orders")
            print("You can do the following: ")
            print("1. Rent a car")
            print("2. Return car")
            print("3. Current orders")
            print("4. Completed orders")
            print("5. Revoke order")
            print("6. Edit order")
            print("7. List order history of car")
            print("8. List order history of customer")
            print("\n""\33[;31mPress q to go back \33[;0m")

            action = input("\nChoose an option: ")
            if action == '1':
                self.rent_car()

            elif action == '2':
                self.return_car()

            elif action == '3':
                self.header("Current orders")
                orders = self.__order_service.get_orders()
                if orders:
                    self.__order_service.print_current_orders(orders)
                else:
                    print("\nNo orders\n")
                input("\33[;32mPress enter to continue \33[;0m")

            elif action == '4':
                self.completed_orders()

            elif action == '5':
                self.revoke_order()

            elif action == '6':
                self.edit_current_order()

            elif action == "7":
                self.history_of_car()

            elif action == '8':
                self.get_order_history_of_customer()
