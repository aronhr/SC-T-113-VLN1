from services.CarService import CarService
from modules.car.Car import Car
import string
import os


class CarUi:

    def __init__(self):
        self.__car_service = CarService()

    def print_cars(self, cars):
        print("{:^5}|{:^12}|{:^12}|{:^10}|{:^7}|{:^7}|{:^14}|{:^11}|{:^15}|{:^14}|{:^14}".format("Id", "Brand", "Type", "Class",
                                                                                   "Seats", "4x4", "Transmission",
                                                                                   "Available", "Price per day", "In rent from", "In rent to"))
        print("-" * 130)
        for ix, car in enumerate(cars):
            print("{:<7}{:<13}{:<14}{:<12}{:<6}{:<9}{:<14}{:<11}{:<17}{:<14}{:<14}".format(ix + 1, car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"], car["Status"], car["Price"] + " kr.", car["FromDate"], car["ToDate"]))

    def main_menu(self):
        remove_punct_map = dict.fromkeys(map(ord, string.punctuation))
        action = ""
        while action != "q":
            os.system('cls')
            print("1. Available cars")
            print("2. Cars in rent")
            print("3. Available cars within date")
            print("4. All cars")
            print("5. Create new car")
            print("6. Edit car")
            print("7. Remove car")
            print("press q to quit")

            action = input("Choose an option: ").lower()
            if action == "1":
                try:
                    cars = self.__car_service.get_available_cars()
                    self.print_cars(cars)
                    input("Press enter to continue")
                except Exception:
                    print("No available car exists")
            elif action == "2":
                try:
                    cars = self.__car_service.get_not_available_cars()
                    self.print_cars(cars)
                    input("Press enter to continue")
                except Exception:
                    print("No unavailable car exists")
            elif action == "3":
                try:
                    from_date = self.__car_service.user_date("Enter date from (dd/mm/yy): ")
                    to_date = self.__car_service.user_date("Enter date to (dd/mm/yy): ")
                    cars = self.__car_service.get_available_date_cars(from_date, to_date)
                    self.print_cars(cars)
                    input("Press enter to continue")
                except Exception:
                    print("No available car exists at that time")
            elif action == "4":
                try:
                    cars = self.__car_service.get_cars()
                    self.print_cars(cars)
                    input("Press enter to continue")
                except Exception:
                    print("No cars exists")
            elif action == "5":
                try:
                    model = input("Model: ").translate(remove_punct_map)
                    cartype = input("Type: ").translate(remove_punct_map)
                    carclass = input("Class: ").translate(remove_punct_map)
                    seats = input("How many seats: ").translate(remove_punct_map)
                    fwd = input("4x4 (Y/N): ").upper().translate(remove_punct_map)
                    transmission = input("Transmission (A/M): ").upper().translate(remove_punct_map)
                    new_car = Car(model, cartype, carclass, seats, fwd, transmission)
                    self.__car_service.add_car(new_car)
                    print(new_car)
                    input("Press enter to continue")
                except Exception:
                    print("Wow, how did you do that?")

            elif action == "6":
                try:
                    cars = self.__car_service.get_cars()
                    self.print_cars(cars)
                    c_id = int(input("Select car by Id: "))
                    car = self.__car_service.get_car_by_id(c_id)
                    self.print_cars([car])
                    car = Car(car["Model"], car["Type"], car["Class"], car["Seats"], car["4x4"], car["Transmission"], int(car["Price"]), car["Status"], car["FromDate"], car["ToDate"])

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
                            car.set_4x4(input("Enter new 4x4 (Y / N): ").upper().translate(remove_punct_map))
                        elif choice == "6":
                            car.set_transmission(input("Enter new Transmission (A / M): ").upper().translate(remove_punct_map))
                        elif choice == "7":
                            car.set_status(input("Enter new status: (T / F): ").upper().translate(remove_punct_map))
                    self.__car_service.remove_car(c_id)
                    self.__car_service.add_car(car)
                    print(car)
                    input("Press enter to continue")
                except Exception:
                    print("Something went wrong, please try again")

            elif action == "7":
                try:
                    cars = self.__car_service.get_cars()
                    self.print_cars(cars)
                    c_id = int(input("Select car by Id: "))
                    car = self.__car_service.get_car_by_id(c_id)
                    self.print_cars([car])
                    self.__car_service.remove_car(c_id)
                    input("Press enter to continue")
                except Exception:
                    print("Something went wrong, please try again")
