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

    def print_cars(self, cars):
        print("{:^6}|{:^12}|{:^12}|{:^10}|{:^7}|{:^7}|{:^14}|{:^11}|{:^15}|{:^9}".format
              ("Id", "Brand", "Type", "Class", "Seats", "4x4", "Transmission", "Available", "Price per day", "License"))
        print("-" * 112)
        for ix, car in enumerate(cars):
            print("{:^8}{:<13}{:<14}{:<12}{:<6}{:<9}{:<14}{:<11}{:<17}{:<9}".format
                  (ix + 1, car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"],
                   car["Status"], car["Price"] + " kr.", car["License"]))

    def print_price(self, cars):
        print("{:^10}|{:^10}|{:^17}|{:^13}".format("Class", "Price", "Extra Insurance", "Total price"))
        print("-"*53)
        arr = []
        for car in cars:
            if car["Class"] not in arr:
                print("{:<10} {:>4} {:<3} {:>14} {:<3} {:>10} {:<3}".format(car["Class"], car["Price"], "kr.", (int(car["Price"]) * 0.75), "kr.", (int(car["Price"]) * 1.75), "kr."))
                arr.append(car["Class"])

    def list_available_cars(self):
        try:
            cars = self.__car_service.get_available_cars()
            self.print_cars(cars)
        except Exception:
            print("\nNo available car exists\n")
        input("Press enter to continue")

    def list_cars_in_rent(self):
        try:
            cars = self.__car_service.get_not_available_cars()
            self.print_cars(cars)
        except Exception:
            print("\nNo unavailable car exists\n")
        input("Press enter to continue")

    def cars_within_date(self):
        if self.__car_service.get_cars() == "Add some cars to start with":
            print("\nNo car exist\n")
        else:
            try:
                from_date = self.__car_service.user_date("\nEnter date from (dd/mm/yy): ")
                to_date = self.__car_service.user_date("Enter date to (dd/mm/yy): ")
                cars = self.__car_service.get_available_date_cars(from_date, to_date)
                self.print_cars(cars)
            except Exception as e:
                print("\nNo available car exists at that time\n")
                print(e)
        input("Press enter to continue")

    def list_all_cars(self):
        if self.__car_service.get_cars() == "Add some cars to start with":
            print("\nNo car exist\n")
        else:
            try:
                cars = self.__car_service.get_cars()
                self.print_cars(cars)
            except Exception:
                print("\nNo car exists\n")
        input("Press enter to continue")

    def price_list(self):
        if self.__car_service.get_cars() == "Add some cars to start with":
            print("\nNo car exist\n")
        else:
            try:
                cars = self.__car_service.get_cars()
                self.print_price(cars)
            except Exception:
                print("\nSome thing went wrong\n")
        input("Press enter to continue")

    def create_new_car(self):
        try:
            print("Creating car:")
            license_plate = input("Enter license plate (q to quit): ").lower()
            if license_plate == "q":
                pass
            else:
                with urllib.request.urlopen("http://apis.is/car?number=" + license_plate) as url:
                    car = json.loads(url.read())
                    car = car["results"][0]
                    model = car["type"].split()[0].capitalize()
                    subtype = car["subType"].capitalize()
                    print("{}\tSelected car Type: {}, SubType: {}{}".format("\33[;92m", model, subtype, "\33[;0m"))
                    if input("Do you want to select another car(Y/N): ").upper() == "Y":
                        pass
                carclass = input("\tClass: ").translate(remove_punct_map)
                seats = input("\tHow many seats: ").translate(remove_punct_map)
                fwd = input("\t4x4 (Y/N): ").upper().translate(remove_punct_map)
                transmission = input("\tTransmission (A/M): ").upper().translate(remove_punct_map)

                new_car = Car(model, subtype, carclass, seats, fwd, transmission, car["number"])
                print(new_car)
                if input("Do you want to create this car? (Y/N): ").upper() == "Y":
                    self.__car_service.add_car(new_car)
                    print("Car created!")
                else:
                    print("\nNo car created.\n")
        except Exception:
            print("\nNo car with that license plate!\n")
        input("Press enter to continue")

    def edit_car(self):
        if self.__car_service.get_cars() == "Add some cars to start with":
            print("\nNo car exist\n")
        else:
            try:
                cars = self.__car_service.get_cars()
                self.print_cars(cars)
                c_id = int(input("Select car by Id: "))
                car = self.__car_service.get_car_by_id(c_id)
                self.print_cars([car])
                car = Car(car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"],
                          car["License"], int(car["Price"]), car["Status"])

                choice = ""
                while choice != "q":
                    print("\n1. Edit Brand\n2. Edit Type\n3. Edit Class\n4. Edit Seats\n5. Edit 4x4\n"
                          "6. Edit Transmission\n7. Edit Status\npress q to quit")
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
                self.__car_service.remove_car(c_id)
                self.__car_service.add_car(car)
                print(car)
            except Exception:
                print("\nSomething went wrong, please try again\n")
        input("Press enter to continue")

    def remove_car(self):
        if self.__car_service.get_cars() == "Add some cars to start with":
            print("\nNo car exist\n")
        else:
            try:
                cars = self.__car_service.get_cars()
                self.print_cars(cars)
                c_id = int(input("Select car by Id: "))
                car = self.__car_service.get_car_by_id(c_id)
                self.print_cars([car])
                self.__car_service.remove_car(c_id)
            except Exception:
                print("\nSomething went wrong, please try again\n")
        input("Press enter to continue")

    def main_menu(self):
        action = ""
        while action != "q":
            os.system('cls')
            print("Cars:")
            print("You can do the following: ")
            print("1. Available cars")
            print("2. Cars in rent")
            print("3. Available cars within date")
            print("4. All cars")
            print("5. Price list")
            print("6. Create new car")
            print("7. Edit car")
            print("8. Remove car")
            print("Press q to go back")

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
