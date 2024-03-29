from services.CarService import CarService
from modules.car.Car import Car
import string
import os
import urllib.request
import json

remove_punct_map = dict.fromkeys(map(ord, string.punctuation))


class CarUi:

    def __init__(self):
        self.__car_service = CarService()

    def selecting_car_in_print(self, cars, stat="All"):
        while True:
            car_id = self.print_cars(cars)
            if car_id == 'q':
                break
            car_id = int(car_id)
            try:
                selected_car = self.__car_service.get_car_by_id(car_id, stat)
                print("\n", selected_car["License"])
            except Exception:
                print("\nNo car with that id")
            input("\n\33[;32mPress enter to continue \33[;0m")

    @staticmethod
    def header(i):
        """
        This the the header that we user in the functions in the file
        :param i:
        :return:
        """
        print("-" * 50)
        print("|{:^48}|".format(i))
        print("-" * 50)
        print()

    def print_cars(self, cars):
        """
        Prints the first 10 cars, and then the system will ask you if you want to find more or less customer.
        if the list are bigger than 10
        :param cars:
        :return:
        """
        start = 0
        stop = 10
        count = 1
        while True:
            print("{:^6}|{:^12}|{:^12}|{:^10}|{:^7}|{:^7}|{:^14}|{:^11}|{:^15}|{:^9}".format
                  ("Id", "Brand", "Type", "Class", "Seats", "4x4", "Transmission", "Available", "Price per day", "License"))
            print("-" * 112)
            for ix, car in enumerate(cars[start:stop]):
                print("{:^8}{:<13}{:<13}{:<12}{:<8}{:<7}{:<15}{:<12}{:<16}{:<9}".format
                      (ix + count, car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"],
                       car["Status"], car["Price"] + " kr.", car["License"]))
            print()
            y_n = input("Next / Previous / Quit (N/P/Q) or ID to chose a car: ").lower()
            if y_n.isdigit():
                return y_n
            elif y_n == "n" and count + 10 <= len(cars):
                start, stop, count = self.__car_service.next_list(stop)
            elif y_n == "n" and count + 10 > len(cars):
                print("\nCant go forwards while on the last page\n")
            elif y_n == "p" and count != 1:
                start, stop, count = self.__car_service.prev_list(start)
            elif y_n == 'p' and count == 1:
                print("\nCant go back while on the first page\n")
                continue
            elif y_n == 'q':
                return y_n
            else:
                print("\n\33[;31mWrong input, try again!\33[;0m\n")
                continue

    @staticmethod
    def print_price(cars):
        """
        Prints the price list
        :param cars:
        :return:
        """
        print("{:^10}|{:^10}|{:^17}|{:^15}".format("Class", "Price", "Extra Insurance", "Total price"))
        print("-" * 54)
        arr = []
        for car in cars:
            if car["Class"] not in arr:
                print("{:<9} {:>6} {:<2} {:>14} {:<3} {:>10} {:<2}".format(car["Class"], car["Price"], "kr.",
                                                                            (int(int(car["Price"]) * 0.75)), "kr.",
                                                                            (int(int(car["Price"]) * 1.75)), "kr."))
                arr.append(car["Class"])
        print()

    def list_available_cars(self):
        """
        Lists all the available cars, and cast a message if there is no cars.
        :return:
        """
        self.header("Available cars")
        cars = self.__car_service.get_available_cars()
        if cars:
            self.selecting_car_in_print(cars, "True")
        else:
            print("No available car exists\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def list_cars_in_rent(self):
        """
        List all the cars that are in rental at this moment.
        :return:
        """
        self.header("Unavalible cars")
        cars = self.__car_service.get_not_available_cars()
        if cars:
            self.selecting_car_in_print(cars, "False")
        else:
            print("No unavailable cars exists\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def cars_within_date(self):
        """
        Find available cars within date, and prints out the Available cars,
        or messages you that there is not a car available
        :return:
        """
        self.header("Available cars within date")
        from_date = self.__car_service.user_date("\nEnter date from (dd/mm/yy): ")
        to_date = self.__car_service.user_date("Enter date to (dd/mm/yy): ")
        print()
        cars = self.__car_service.get_available_date_cars_UI(from_date, to_date)
        if cars:
            self.selecting_car_in_print(cars)
        else:
            print("\nNo available cars exists at that time\n")
        input("\33[;32mPress enter to continue\33[;0m")

    def list_all_cars(self):
        """
        Lists all cars by the the "ID", and message you if there is no car to see.
        :return:
        """
        self.header("All cars")
        cars = self.__car_service.get_cars()
        if cars:
            self.selecting_car_in_print(cars)
        else:
            print("No cars exists\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def price_list(self):
        """
        This will add a car to create a price list.
        :return:
        """
        self.header("Price list")
        cars = self.__car_service.get_cars()
        if cars:
            self.print_price(cars)
        else:
            print("Add some cars to create price list\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def create_new_car(self):
        """
        Makes a new car, if you enter a actual car plate that exist we call an api to get the Type and the Subtype
        and asks the customer for more details about the car.
        or it will message you that there is no car with this car plate.
        :return:
        """
        self.header("Create new car")
        try:
            print("Creating car:")
            go = "N"
            while go != "Y":
                try:
                    license_plate = input("Enter license plate (\33[;31mq to quit\33[;0m): ").upper()
                    if license_plate == "Q":
                        break
                    if self.__car_service.get_car_by_license(license_plate):
                        print("Car already exists")
                    else:
                        with urllib.request.urlopen("http://apis.is/car?number=" + license_plate) as url:
                            car = json.loads(url.read())
                            car = car["results"][0]
                            model = car["type"].split()[0].capitalize()
                            subtype = car["subType"].capitalize()

                            print("{}\tSelected car Type: {}, SubType: {}{}".format("\33[;92m", model, subtype, "\33[;0m"))
                            go = input("\tDo you want to select this car (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").upper()
                except Exception:
                    print("\nNo car with that license plate!\n")

            if go == "Y":
                carclass = self.__car_service.check_car_class("\tClass: \n\t\t\33[;36m1. Luxury\n\t\t2. Sport\n\t\t3. Off-road\n\t\t4. Sedan\n\t\t5. Economy\33[;0m\n\tSelect class: ", "\tInvalid input")
                seats = input("\tHow many seats: ").translate(remove_punct_map)
                fwd = input(
                    "\t4x4 (""\33[;32mY\33[;0m/\33[;31mN\33[;0m""): ").upper().translate(
                    remove_punct_map)
                transmission = self.__car_service.transmission("\tTransmission (A/M): ", "\tInvalid input")
                new_car = Car(model, subtype, carclass, seats, fwd, transmission, car["number"])
                print(new_car)
                if input("Do you want to create this car? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").upper() == "Y":
                    self.__car_service.add_car(new_car)
                    print("\nCar created!\n")
                else:
                    print("\nNo car created.\n")
        except Exception:
            print("\n\33[;31mSomething went wrong, please try again!\33[;0m\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def edit_car(self):
        """
        Offer you yo edit an specific car by id.
        then you can edit a specific thing about the car (e. Type).
        or tells you that the id of the car is not in the csv file.
        :return:
        """
        self.header("Edit car")
        cars = self.__car_service.get_cars()
        if cars:
            c_id = self.print_cars(cars)
            if c_id != "q":
                try:
                    car = self.__car_service.get_car_by_id(int(c_id))
                    car = Car(car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"],
                              car["License"], int(car["Price"]), car["Status"])

                    choice = ""
                    while choice != "q":
                        print("\n1. Edit Brand\n2. Edit Type\n3. Edit Class\n4. Edit Seats\n5. Edit 4x4\n"
                              "6. Edit Transmission\n7. Edit Status\n\n\33[;31mpress q to go back\33[;0m\n")
                        choice = input("Enter your choice: ").lower()
                        if choice == "1":
                            car.set_model(input("Enter new Brand: ").translate(remove_punct_map))
                        elif choice == "2":
                            car.set_type(input("Enter new Type: ").translate(remove_punct_map))
                        elif choice == "3":
                            car.set_class(self.__car_service.check_car_class("Enter new class: \n\t\33[;36m1. Luxury\n\t2. Sport\n\t3. Off-road\n\t4. Sedan\n\t5. Economy\33[;0m\nSelect class: ", "Invalid input"))
                        elif choice == "4":
                            car.set_seats(input("Enter Seats: ").translate(remove_punct_map))
                        elif choice == "5":
                            car.set_4x4(input("Enter new 4x4 (Y/N): ").upper().translate(remove_punct_map))
                        elif choice == "6":
                            car.set_transmission(self.__car_service.transmission("Enter new Transmission (A/M): ", "Invalid input"))
                        elif choice == "7":
                            car.set_status(input("Enter new status: (\33[;32mT\33[;0m/\33[;31mF\33[;0m): ").upper().translate(remove_punct_map))

                    self.__car_service.remove_car(int(c_id))
                    self.__car_service.add_car(car)
                    print("\nThe car has been edited\n")
                    print(car)

                except Exception:
                    print("\33[;31mNo car with that ID, try again!\33[;0m")
        else:
            print("No cars exists\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def remove_car(self):
        """
        Asks the customer for an id and deletes the csv file, and return the csv file like it was before without the
        car that the customer selected by id
        :return:
        """
        self.header("Remove car")
        cars = self.__car_service.get_cars()
        if cars:
            c_id = self.print_cars(cars)
            if c_id != "q":
                try:
                    are_you_sure = input("Are you sure you want to delete this car? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if are_you_sure == "y":
                        car = self.__car_service.get_car_by_id(int(c_id))
                        self.print_cars([car])
                        print("Car number {} has been deleted\n".format(c_id))
                        self.__car_service.remove_car(int(c_id))
                except Exception:
                    print("\33[;31mWrong input, try again!\33[;0m")
        else:
            print("No cars exists\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def main_menu(self):
        """
        This the main menu for the Car user interface. it offer you to (e. list all the cars in rental)
        :return:
        """
        action = ""
        while action != "q":
            os.system('cls')
            self.header("Cars")
            print("You can do the following: \n1. Available cars\n2. Unavailable cars\n"
                  "3. Available cars within date range""\n4. All cars\n5. Price list\n6. Create new car\n"
                  "7. Edit car\n8. Remove car\n\n""\33[;31mPress q to go back \33[;0m")

            action = input("\nChoose an option: ").lower()

            if action == "1":
                self.list_available_cars()
            elif action == "2":
                self.list_cars_in_rent()
            elif action == "3":
                self.cars_within_date()
            elif action == "4":
                self.list_all_cars()
            elif action == "5":
                self.price_list()
            elif action == "6":
                self.create_new_car()
            elif action == "7":
                self.edit_car()
            elif action == "8":
                self.remove_car()
