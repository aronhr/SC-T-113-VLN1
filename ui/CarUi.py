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

    @staticmethod
    def print_cars(cars):
        print("{:^6}|{:^12}|{:^12}|{:^10}|{:^7}|{:^7}|{:^14}|{:^11}|{:^15}|{:^9}".format
              ("Id", "Brand", "Type", "Class", "Seats", "4x4", "Transmission", "Available", "Price per day", "License"))
        print("-" * 112)
        for ix, car in enumerate(cars):
            print("{:^8}{:<13}{:<14}{:<12}{:<6}{:<9}{:<14}{:<11}{:<17}{:<9}".format
                  (ix + 1, car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"],
                   car["Status"], car["Price"] + " kr.", car["License"]))
        print()

    @staticmethod
    def print_price(cars):
        print("{:^10}|{:^10}|{:^17}|{:^13}".format("Class", "Price", "Extra Insurance", "Total price"))
        print("-" * 53)
        arr = []
        for car in cars:
            if car["Class"] not in arr:
                print("{:<10} {:>4} {:<3} {:>14} {:<3} {:>10} {:<3}".format(car["Class"], car["Price"], "kr.",
                                                                            (int(car["Price"]) * 0.75), "kr.",
                                                                            (int(car["Price"]) * 1.75), "kr."))
                arr.append(car["Class"])
        print()

    def list_available_cars(self):
        cars = self.__car_service.get_available_cars()
        if cars:
            self.print_cars(cars)
        else:
            print("\nNo available car exists\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def list_cars_in_rent(self):
        cars = self.__car_service.get_not_available_cars()
        if cars:
            self.print_cars(cars)
        else:
            print("\nNo unavailable cars exists\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def cars_within_date(self):
        from_date = self.__car_service.user_date("\nEnter date from (dd/mm/yy): ")
        to_date = self.__car_service.user_date("Enter date to (dd/mm/yy): ")
        cars = self.__car_service.get_available_date_cars(from_date, to_date)
        if cars:
            self.print_cars(cars)
        else:
            print("\nNo available cars exists at that time\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def list_all_cars(self):
        cars = self.__car_service.get_cars()
        if cars:
            self.print_cars(cars)
        else:
            print("\nNo cars exists\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def price_list(self):
        cars = self.__car_service.get_cars()
        if cars:
            self.print_price(cars)
        else:
            print("\nAdd some cars to create price list\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def create_new_car(self):
        try:
            print("Creating car:")
            go = "N"
            while go != "Y":
                try:
                    license_plate = input("Enter license plate ((\33[;31mq to quit\33[;0m):").lower()
                    if license_plate == "q":
                        break
                    with urllib.request.urlopen("http://apis.is/car?number=" + license_plate) as url:
                        car = json.loads(url.read())
                        car = car["results"][0]
                        model = car["type"].split()[0].capitalize()
                        subtype = car["subType"].capitalize()

                        print("{}\tSelected car Type: {}, SubType: {}{}".format("\33[;92m", model, subtype, "\33[;0m"))
                        go = input("\tDo you want to select this car (Y/N): ").upper()
                except Exception:
                    print("\nNo car with that license plate!\n")

            if go == "Y":
                carclass = input("\tClass: ").translate(remove_punct_map)
                seats = input("\tHow many seats: ").translate(remove_punct_map)
                fwd = input(
                    "\t4x4 (""\33[;32mY\33[;0m/\33[;31mN\33[;0m"")").upper().translate(
                    remove_punct_map)
                transmission = input("\tTransmission (A/M): ").upper().translate(remove_punct_map)
                new_car = Car(model, subtype, carclass, seats, fwd, transmission, car["number"])
                print(new_car)
                if input(
                        "Do you want to create this car? (\33[;32mY\33[;0m/\33[;31mN\33[;0m").upper() == "Y":
                    self.__car_service.add_car(new_car)
                    print("\nCar created!\n")
                else:
                    print("\nNo car created.\n")
        except Exception:
            print("\nSomething went wrong, please try again!\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def edit_car(self):
        cars = self.__car_service.get_cars()
        if cars:
            self.print_cars(cars)
            c_id = input("Select car by Id (\33[;31mq to go back\33[;0m): ").lower()
            if c_id != "q":
                try:
                    car = self.__car_service.get_car_by_id(int(c_id))
                    self.print_cars([car])
                    car = Car(car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"],
                              car["License"], int(car["Price"]), car["Status"])

                    choice = ""
                    while choice != "q":
                        print("\n1. Edit Brand\n2. Edit Type\n3. Edit Class\n4. Edit Seats\n5. Edit 4x4\n"
                              "6. Edit Transmission\n7. Edit Status\n\33[;31mpress q to go back\33[;0m")
                        choice = input("Enter your choice: ").lower()
                        if choice == "1":
                            car.set_model(input("Enter new Brand: ").translate(remove_punct_map))
                        elif choice == "2":
                            car.set_type(input("Enter new Type: ").translate(remove_punct_map))
                        elif choice == "3":
                            car.set_class(input("Enter new Class: ").translate(remove_punct_map))
                        elif choice == "4":
                            car.set_seats(input("Enter Seats: ").translate(remove_punct_map))
                        elif choice == "5":
                            car.set_4x4(input("Enter new 4x4 (Y/N): ").upper().translate(remove_punct_map))
                        elif choice == "6":
                            car.set_transmission(
                                input("Enter new Transmission (A/M): ").upper().translate(remove_punct_map))
                        elif choice == "7":
                            car.set_status(input("Enter new status: (T/F): ").upper().translate(remove_punct_map))
                    self.__car_service.remove_car(int(c_id))
                    self.__car_service.add_car(car)
                    print("\nThe car has been edited\n")
                    print(car)

                except Exception:
                    print("Wrong input, try again")
        else:
            print("\nNo cars exists\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def remove_car(self):
        cars = self.__car_service.get_cars()
        if cars:
            self.print_cars(cars)
            c_id = input("Select car by Id (\33[;31mPress q to go back\33[;0m): ").lower()
            if c_id != "q":
                try:
                    are_you_sure = input("Are you sure you want to delete this car? (\33[;32mY\33[;0m/\33[;31mN\33[;0m): ").lower()
                    if are_you_sure == "y":
                        car = self.__car_service.get_car_by_id(int(c_id))
                        self.print_cars([car])
                        print("Car number {} has been deleted".format(c_id))
                        self.__car_service.remove_car(int(c_id))
                except Exception:
                    print("Wrong input, try again")
        else:
            print("\nNo cars exists\n")
        input("\33[;32mPress enter to continue \33[;0m")

    def main_menu(self):
        action = ""
        while action != "q":
            os.system('cls')
            print("Cars:")
            print("You can do the following: \n1. Available cars\n2. Unavailable cars\n3. Available cars within date"
                  "\n4. All cars\n5. Price list\n6. Create new car\n7. Edit car\n8. Remove car\n\n""\33[;31mPress q to go back \33[;0m")

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
