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
            if car["Status"] == "True":
                status = "\33[;32m" + car["Status"] + "\33[;0m"
            else:
                status = "\33[;31m" + car["Status"] + "\33[;0m"
            print("{:^8}{:<13}{:<14}{:<12}{:<6}{:<9}{:<14}{:<11}{:<17}{:<9}".format
                  (ix + 1, car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"],
                   status, car["Price"] + " kr.", car["License"]))

    def print_price(self, cars):
        print("{:^10}|{:^10}|{:^17}|{:^13}".format("Class", "Price", "Extra Insurance", "Total price"))
        print("-"*53)
        arr = []
        for car in cars:
            if car["Class"] not in arr:
                print("{:<10} {:>4} {:<3} {:>14} {:<3} {:>10} {:<3}".format(car["Class"], car["Price"], "kr.", (int(car["Price"]) * 0.75), "kr.", (int(car["Price"]) * 1.75), "kr."))
                arr.append(car["Class"])

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
            print("\33[;31m" + "press q to quit" + "\33[;0m")

            action = input("Choose an option: ").lower()
            if action == "1":
                try:
                    cars = self.__car_service.get_available_cars()
                    self.print_cars(cars)
                    input("\33[;32m" + "press enter to continue" + "\33[;0m")
                except Exception:
                    print("No available car exists")
            elif action == "2":
                try:
                    cars = self.__car_service.get_not_available_cars()
                    self.print_cars(cars)
                    input("\33[;32m" + "Press enter to continue " + "\33[;0m")
                except Exception:
                    print("No unavailable car exists")
            elif action == "3":
                try:
                    from_date = self.__car_service.user_date("Enter date from (dd/mm/yy): ")
                    to_date = self.__car_service.user_date("Enter date to (dd/mm/yy): ")
                    cars = self.__car_service.get_available_date_cars(from_date, to_date)
                    self.print_cars(cars)
                    input("\33[;32m" + "Press enter to continue " + "\33[;0m")
                except Exception as e:
                    print("No available car exists at that time")
                    print(e)
            elif action == "4":
                try:
                    cars = self.__car_service.get_cars()
                    self.print_cars(cars)
                    input("\33[;32m" + "Press enter to continue " + "\33[;0m")
                except Exception:
                    print("No cars exists")
            elif action == "5":
                # Price list
                try:
                    cars = self.__car_service.get_cars()
                    self.print_price(cars)
                    input("\33[;32m" + "Press enter to continue " + "\33[;0m")
                except Exception:
                    print("Some thing went wrong")
            elif action == "6":
                try:
                    print("Creating car:")
                    license_plate = input("Enter license plate (""\33[;31m" + " q to quit" + "\33[;0m""):").lower()
                    if license_plate == "q":
                        continue
                    else:
                        with urllib.request.urlopen("http://apis.is/car?number=" + license_plate) as url:
                            car = json.loads(url.read())
                            car = car["results"][0]
                            model = car["type"].split()[0].capitalize()
                            subtype = car["subType"].capitalize()
                            print("{}\tSelected car Type: {}, SubType: {}{}".format("\33[;92m", model, subtype, "\33[;0m"))
                            if input("Do you want to select another car(Y/N): ").upper() == "Y":
                                continue
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
                            print("No car created.")
                except Exception:
                    print("No car with that license plate!")
                input("\33[;32m" + "Press enter to continue " + "\33[;0m")

            elif action == "7":
                try:
                    cars = self.__car_service.get_cars()
                    self.print_cars(cars)
                    c_id = int(input("Select car by Id: "))
                    car = self.__car_service.get_car_by_id(c_id)
                    self.print_cars([car])
                    car = Car(car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"], car["License"], int(car["Price"]), car["Status"])

                    choice = ""
                    while choice != "q":
                        print("\n1. Edit Brand\n2. Edit Type\n3. Edit Class\n4. Edit Seats\n5. Edit 4x4\n"
                              "6. Edit Transmission\n7. Edit Status\n""\33[;31m" + "press q to quit" + "\33[;0m")
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
                            car.set_transmission(input("Enter new Transmission (A/M): ").upper().translate(remove_punct_map))
                        elif choice == "7":
                            car.set_status(input("Enter new status: (T/F): ").upper().translate(remove_punct_map))
                    self.__car_service.remove_car(c_id)
                    self.__car_service.add_car(car)
                    print(car)
                    input("\33[;32m" + "Press enter to continue " + "\33[;0m")
                except Exception:
                    print("Something went wrong, please try again")

            elif action == "8":
                try:
                    cars = self.__car_service.get_cars()
                    self.print_cars(cars)
                    c_id = int(input("Select car by Id: "))
                    car = self.__car_service.get_car_by_id(c_id)
                    self.print_cars([car])
                    self.__car_service.remove_car(c_id)
                    input("\33[;32m" + "Press enter to continue " + "\33[;0m")
                except Exception:
                    print("Something went wrong, please try again")

