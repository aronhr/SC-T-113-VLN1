from services.CarService import CarService
from modules.car.Car import Car
import string
import os


class CarUi:

    def __init__(self):
        self.__car_service = CarService()

    def print_cars(self, cars):
        print("{:^5}|{:^12}|{:^10}|{:^10}|{:^7}|{:^7}|{:^14}|{:^11}|{:^15}".format("Id", "Brand", "Type", "Class",
                                                                                   "Seats", "4x4", "Transmission",
                                                                                   "Available", "Price per day"))
        print("-" * 97)
        for ix, car in enumerate(cars):
            print("{:<7}{:<13}{:<12}{:<12}{:<6}{:<9}{:<14}{:<11}{} kr.".format(ix + 1, car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"], car["Status"], car["Price"]))

    def main_menu(self):

        action = ""
        while action != "q":
            os.system('cls')
            print("1. Available cars")
            print("2. Cars in rent")
            print("3. All cars")
            print("4. Create new car")
            print("5. Edit car")
            print("6. Remove car")
            print("press q to quit")

            action = input("Choose an option: ").lower()
            if action == "1":
                cars = self.__car_service.get_available_cars()
                self.print_cars(cars)
                input("Press any key to continue")
            elif action == "2":
                cars = self.__car_service.get_not_available_cars()
                self.print_cars(cars)
                input("Press any key to continue")
            elif action == "3":
                cars = self.__car_service.get_cars()
                self.print_cars(cars)
                input("Press any key to continue")
            elif action == "4":
                try:
                    model = input("Model: ").replace(string.punctuation, "")
                    cartype = input("Type: ").replace(string.punctuation, "")
                    carclass = input("Class: ").replace(string.punctuation, "")
                    seats = input("How many seats: ").replace(string.punctuation, "")
                    fwd = input("4x4 (Y/N): ").upper().replace(string.punctuation, "")
                    transmission = input("Transmission (A/M): ").upper().replace(string.punctuation, "")
                    new_car = Car(model, cartype, carclass, seats, fwd, transmission)
                    self.__car_service.add_car(new_car)
                    print(new_car)
                    input("Press any key to continue")
                except Exception:
                    print("Wow, how did you do that?")

            elif action == "5":
                cars = self.__car_service.get_cars()
                self.print_cars(cars)
                c_id = int(input("Select car by Id: "))
                car = self.__car_service.get_car_by_id(c_id)
                self.print_cars([car])
                car = Car(car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"], int(car["Price"]), car["Status"])

                choice = ""
                while choice != "q":
                    print("\n1. Edit Brand\n2. Edit Type\n3. Edit Class\n4. Edit Seats\n5. Edit 4x4\n"
                          "6. Edit Transmission\n7. Edit Status\npress q to quit")
                    choice = input("Enter your choice: ").lower()
                    if choice == "1":
                        car.set_model(input("Enter new Brand: "))
                    elif choice == "2":
                        car.set_type(input("Enter new Type: "))
                    elif choice == "3":
                        car.set_class(input("Enter new Class: "))
                    elif choice == "4":
                        car.set_seats(input("Enter Seats: "))
                    elif choice == "5":
                        car.set_4x4(input("Enter new 4x4 (Y / N): ").upper())
                    elif choice == "6":
                        car.set_transmission(input("Enter new Transmission (A / M): "))
                    elif choice == "7":
                        car.set_status(input("Enter new status: (T / F): "))
                self.__car_service.remove_car(c_id)
                self.__car_service.add_car(car)
                print(car)
                input("Press any key to continue")

            elif action == "6":
                cars = self.__car_service.get_cars()
                self.print_cars(cars)
                c_id = int(input("Select car by Id: "))
                car = self.__car_service.get_car_by_id(c_id)
                self.print_cars([car])
                self.__car_service.remove_car(c_id)
                input("Press any key to continue")
