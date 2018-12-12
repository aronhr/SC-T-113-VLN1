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
        print("{:^6}|{:^12}|{:^20}|{:^17}|{:^21}|{:^21}|{:^12}|{:^11}|{:^13}|{:^6}".format
              ("ID", "Kt", "Name", "Car-license", "From date", "To date", "Price", "Insurance", "Total price", "Days"))
        print("-" * 149)
        for ix, order in enumerate(orders):
            print("{:^8} {:^12} {:<20} {:<19} {:<24} {:<18} {:<12} {:<11} {:<13} {:<6}".format
                  (ix + 1, order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                   order["Price"], order["Insurance"], order["Total price"], order["Days"]))
        print()

    @staticmethod
    def print_completed_orders(completed_orders):
        print("{:^6}|{:^12}|{:^20}|{:^17}|{:^21}|{:^21}|{:^20}|{:^21}|{:^11}|{:^13}|{:^6}".format
              ("ID", "Kt", "Name", "License", "From date", "To date", "Price", "Payment method", "Insurance",
               "Total price", "Days"))

        print("-" * 180)
        for ix, order in enumerate(completed_orders):
            print("{:^6}  {:<12}  {:<20}  {:<17}  {:<21}  {:<21}  {:<20}  {:<21} {:<11} {:<13} {:<6}".format
                  (ix + 1, order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                   order["Price"], order["Payment method"], order["Insurance"], order["Total price"], order["Days"]))
        print()

    def print_receipt(self, order):
        car = self.__car_service.get_car_by_license(order["License"])
        customer = self.__customer_service.get_customer_by_kt(order["Kt"])

        receipt = """
Customer

    Kt/Passport number: {i:<30}
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
            i_price = int(car["Price"]) * 0.75
            t_price = (int(car["Price"]) * 0.75) * int(order["Days"])

        output = receipt.format(i=customer["Passport number"], name=customer["Name"], mail=customer["Mail"],
                                address=customer["Address"], country=customer["Country"],
                                license=customer["license"],
                                age=customer["Age"], phone=customer["Phone number"], car_license=car["License"],
                                car_model=car["Model"], car_type=car["Type"], car_class=car["Class"],
                                car_seats=car["Seats"], car_fwd=car["4x4"], car_transmission=car["Transmission"],
                                car_price=car["Price"], price=order["Price"], order_insurance=order["Insurance"],
                                order_days=order["Days"], order_price=order["Total price"],
                                car_order_price=(int(car["Price"]) * int(order["Days"])),
                                insurance_order_price=t_price,
                                insurance_price=i_price, from_day=order["From date"], to_day=order["To date"],
                                order_penalty=order["Penalty"])
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

    @staticmethod
    def calculate_days(from_date, to_date):
        # Calculate how long the order is in days
        from_date = datetime.datetime.date(from_date)
        to_date = datetime.datetime.date(to_date)
        delta = to_date - from_date
        return delta.days  # how many days the rental is

    def create_customer(self, kt):
        name = input("\tEnter name: ").translate(remove_punct_map)
        country = input("\tEnter country: ").translate(remove_punct_map)
        address = input("\tEnter address: ").translate(remove_punct_map)
        mail = input("\tEnter mail: ").strip()
        phone = input("\tEnter phone number: ").translate(remove_punct_map)
        customer_license = input("\tEnter drivers license: ").translate(remove_punct_map)
        age = int(input("\tEnter age: "))
        new_customer = Customer(name, kt, country, address, mail, phone, customer_license, age)
        self.__customer_service.add_customer(new_customer)

    def print_car_types(self):
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
        print("-" * 50)
        print("|{:^48}|".format("Rent car"))
        print("-" * 50)

        kt = input("\tEnter Kt/Passport number: ").translate(remove_punct_map)
        customer = self.__order_service.check_kt(kt)

        if customer:
            self.print_customer(customer)
        else:
            self.create_customer(kt)

        approved = False
        while not approved:
            try:
                from_date = self.__car_service.user_date("\tEnter start date for rent (dd/mm/yy): ")
                to_date = self.__car_service.user_date("\tEnter end date for rent (dd/mm/yy): ")

                if not self.print_car_types():
                    print("\n\tNo available cars")
                    break

                car_type = input("\tEnter type of car (""\33[;31m" + " q to quit" + "\33[;0m""):").translate(remove_punct_map)
                if car_type.upper() == "Q":
                    break

                print("Available cars\n")
                # TODO: If no cars are available all cars that are not available gets printed out!
                available_cars_type = self.__car_service.get_available_date_type(car_type, from_date, to_date)

                if not available_cars_type:
                    i = input("No cars available,(""\33[;31m" + "press q to quit" + "\33[;0m"+","+"\33[;32m" + "enter to select another date " + "\33[;0m"")")
                    if i == "q":
                        break
                else:
                    while not approved:
                        self.__car_ui.print_cars(available_cars_type)
                        try:
                            c_id = input("\nSelect car by Id (""\33[;31m" + " q to quit" + "\33[;0m""):").upper()
                            if c_id == "Q":
                                approved = True
                                break

                            c_id = int(c_id)
                            self.__car_ui.print_cars([available_cars_type[c_id - 1]])

                            chosen_car_plate = available_cars_type[c_id - 1]["License"]
                            price_of_order = int(available_cars_type[c_id - 1]["Price"])

                            days = self.calculate_days(from_date, to_date)

                            price_of_order_days = price_of_order * days     # Price for car multiplied with days

                            print("Price of order: {} ISK".format(price_of_order_days))
                            insurance = input("Would you like extra insurance for {} ISK per day? ""\33[;32m" +"Y"+ "\33[;0m"+"/"+"\33[;31m" +"N"+"\33[;0m".format(int(price_of_order) * 0.75)).upper()    # Insurance (Yes or No)
                            price_of_order_days_insurance = price_of_order_days

                            if insurance == 'Y':
                                price_of_order_days_insurance = price_of_order_days * 1.75  # Price of order with extra insurance
                                print("Price of order: {} ISK".format(price_of_order_days_insurance))
                                deposit = price_of_order_days_insurance * 0.10
                            else:
                                deposit = price_of_order_days * 0.10

                            print("Your deposit of the order is {} ISK".format(deposit))

                            book = input("Order car? \33[;32m" +"Y"+ "\33[;0m"+"/"+"\33[;31m" +"N"+"\33[;0m").upper()
                            if book == 'Y':
                                if customer:
                                    name = customer["Name"]

                                new_order = Order(kt, name, chosen_car_plate, from_date, to_date, price_of_order_days, insurance, price_of_order_days_insurance, days)
                                self.__order_service.add_order(new_order, False)
                                print("\nOrder successful!\n")
                                approved = True
                            else:
                                print("\nOrder canceled!\n")
                        except IndexError:
                            print("ID not available")
            except Exception:
                print("\nNo cars available\n")
                break
        input("\33[;32m" + "Press enter to continue " + "\33[;0m")

    def return_car(self):
        #try:
        orders = self.__order_service.get_orders()
        if orders:
            self.print_current_orders(orders)
            o_id = input("Select order by Id: ")
            order = self.__order_service.get_order_by_id(int(o_id))
            current_order = Order(order["Kt"], order["Name"], order["License"], order["From date"], order["To date"], order["Price"], order["Insurance"], order["Total price"], order["Days"])
            self.print_current_orders([order])
            price = float(order["Total price"])
            km_length = int(input("Enter the km driven: "))
            max_km = 100 * int(order["Days"])
            penalty = 0
            if km_length > max_km:
                for x in range(km_length - max_km):
                    penalty += price * 0.01
            current_order.set_price_insurance(price+penalty)
            current_order.set_penalty(penalty)
            self.__order_service.remove_order(o_id)
            self.__order_service.add_order(current_order, True)
            order = self.__order_service.get_order_by_id(int(o_id))
            self.print_receipt(order)
            if self.__order_service.pay_order(round(price), order):
                self.__order_service.remove_order(int(o_id))
                print("Car Returned!")
            else:
                print("Car payment not accepted!")
        else:
            print("\nNo cars in rent\n")
        #except Exception:
        #    print("Something went wrong, please try again")

    def revoke_order(self):
        try:
            orders = self.__order_service.get_orders()
            if orders:
                self.print_current_orders(orders)
                o_id = int(input("Select order by Id (""\33[;31m" + " q to quit" + "\33[;0m""):"))
                order = self.__order_service.get_order_by_id(o_id)
                self.print_current_orders([order])
                total_price = float(order["Total price"])
                print("Your deposit was {} ISK".format(int(total_price * 0.10)))
                choice = input("Are you sure you want to revoke the order? ""\33[;32m" +"Y"+ "\33[;0m"+"/"+"\33[;31m" +"N"+"\33[;0m").lower()
                if choice == 'y':
                    self.__order_service.remove_order(o_id)
                    print("Order revoked and deposit returned")
                elif choice == 'n':
                    print("Revoke canceled")
            else:
                print("\nNo orders\n")
        except Exception:
            print("Revoke Canceled")
        input("\33[;32m" + "Press enter to continue " + "\33[;0m")

    def edit_current_order(self):
        orders = self.__order_service.get_orders()
        if orders:
            self.print_current_orders(orders)
            o_id = int(input("Select order by Id: "))
            order = self.__order_service.get_order_by_id(o_id)
            edited_order = Order(order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                                 order["Price"], order["Insurance"], order["Total price"], order["Days"])
            a_choice = ''
            while a_choice != 'q':
                print("1. Edit name\n2. Car-license\n3. From date\n4. To date\n5. Price\n6. Insurance\n7. Days\n""\33[;31m" + "Press q to go back " + "\33[;0m")
                a_choice = input("Choose an option: ").lower()
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
                elif a_choice == '6':
                    edited_order.set_insurance(input("Enter new insurance  YES/NO: ").translate(remove_punct_map))
                elif a_choice == '7':
                    edited_order.set_days(input("Enter number of days: ").translate(remove_punct_map))
            print(edited_order)
            self.__order_service.remove_order(o_id)
            self.__order_service.add_order(edited_order, True)
            print("\nOrder edited\n")
        else:
            print("\nNo orders to edit\n")

    def edit_completed_order(self):
        orders = self.__order_service.get_completed_orders()
        if orders:
            self.print_completed_orders(orders)
            o_id = int(input("Select order by Id: "))
            order = self.__order_service.get_order_by_id(o_id)
            edited_order = Order(order["Kt"], order["Name"], order["License"], order["From date"], order["To date"],
                                 order["Price"], order["Payment method"], order["Insurance"], order["Total price"], order["Days"], )
            choice = ''
            while choice != 'q':
                choice = input(
                    "What do you want to edit?\n1. Name\n2. License\n3. From Date\n4. To date\n5. Price\n6. "
                    "Payment method\n""\33[;31m" + "Press q to go back " + "\33[;0m").lower()
                if choice == '1':
                    edited_order.set_renter(input("Enter new name: ").translate(remove_punct_map))
                elif choice == '2':
                    edited_order.set_car(input("Enter new license: ").translate(remove_punct_map))
                elif choice == '3':
                    edited_order.set_from_date(
                        datetime.datetime.strftime(self.__car_service.user_date("Enter new from date: "), "%d/%m/%y"))
                elif choice == '4':
                    edited_order.set_to_date(
                        datetime.datetime.strftime(self.__car_service.user_date("Enter new to date: "), "%d/%m/%y"))
                elif choice == '5':
                    edited_order.set_price(input("Enter new price: ").translate(remove_punct_map))
                elif choice == '6':
                    edited_order.set_payment_method(input("Enter new payment method: ").translate(remove_punct_map))
                elif choice == '7':
                    edited_order.set_insurance(input("Enter new insurance YES/NO: ").translate(remove_punct_map))
                elif choice == '8':
                    edited_order.set_days(input("Enter the number of days: ").translate(remove_punct_map))

            self.__order_service.remove_order(o_id)
            self.__order_service.add_order(edited_order, True)
        else:
            print("\nNo orders\n")
        input("\33[;32m" + "Press enter to continue " + "\33[;0m")

    def get_order_history_of_customer(self):
        kt = input("Enter passport number of the customer(""\33[;31m" + " q to go back" + "\33[;0m""):").upper()
        if kt != "Q":
            orders = self.__order_service.get_available_order_customer(kt)
            self.print_completed_orders(orders)
        input("\33[;32m" + "Press enter to continue " + "\33[;0m")

    def edit_order(self):
        print("1. Edit current orders\n2. Edit completed orders\n""\33[;31m" + "Press q to go back " + "\33[;0m")
        e_action = input("\nChoose an option: ").upper()
        if e_action != "Q":
            if e_action == '1':
                self.edit_current_order()
            elif e_action == '2':
                self.edit_completed_order()
        input("\33[;32m" + "Press enter to continue " + "\33[;0m")

    def history_of_car(self):
        license = input("Enter car license plate (""\33[;31m" + " q to go back" + "\33[;0m""):").upper()
        if license != "Q":
            orders = self.__order_service.get_available_orders(license)
            self.print_completed_orders(orders)
        input("\33[;32m" + "Press enter to continue " + "\33[;0m")

    def completed_orders(self):
        try:
            completed_orders = self.__order_service.get_completed_orders()
            if self.print_completed_orders(completed_orders) == "No orders":
                o_id = ''
                while o_id != 'q':
                    o_id = input("Select the order you want to view (""\33[;31m" + " q to go back" + "\33[;0m""):")
                    os.system('cls')
                    order = self.__order_service.get_completed_order_id(int(o_id))
                    self.print_receipt(order)
        except Exception:
            print("Something went wrong")
        input("\33[;32m" + "Press enter to continue " + "\33[;0m")

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
            print("8. List order history of customer")
            print("\33[;31m" + "Press q to go back" + "\33[;0m")

            action = input("\nChoose an option: ")
            if action == '1':
                self.rent_car()

            elif action == '2':
                self.return_car()
                input("\33[;32m" + "Press enter to continue " + "\33[;0m")

            elif action == '3':
                orders = self.__order_service.get_orders()
                self.print_current_orders(orders)
                input("\33[;32m" + "Press enter to continue " + "\33[;0m")

            elif action == '4':
                self.completed_orders()

            elif action == '5':
                self.revoke_order()

            elif action == '6':
                self.edit_order()

            elif action == "7":
                self.history_of_car()

            elif action == '8':
                self.get_order_history_of_customer()
