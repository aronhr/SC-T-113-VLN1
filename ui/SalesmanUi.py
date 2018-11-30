from services.CarService import CarService
from modules.car.Car import Car
import string
import os


class SalesmanUi:

    def __init__(self):
        self.__car_service = CarService()

    def main_menu(self):

        action = ""
        while action != "q":
            os.system('cls')
            print("1. Available cars")
            print("2. Cars in rent")
            print("3. All cars")
            print("4. Register new car")
            print("press q to quit")

            action = input("Choose an option: ").lower()
            if action == "1":
                cars = self.__car_service.get_available_cars()
                print(cars)
            elif action == "2":
                cars = self.__car_service.get_not_available_cars()
                print(cars)
            elif action == "3":
                cars = self.__car_service.get_cars()
                print(cars)
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
                except Exception:
                    print("Wow, how did you do that?")
