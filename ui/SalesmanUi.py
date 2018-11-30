from services.CarService import CarService
from modules.car.Car import Car


class SalesmanUi:

    def __init__(self):
        self.__car_service = CarService()

    def main_menu(self):

        action = ""
        while action != "q":
            print("You can do the following: ")
            print("1. Add a car")
            print("2. List all cars")
            print("press q to quit")

            action = input("Choose an option: ").lower()

            if action == "1":
                id = input("Id: ")
                model = input("Model: ")
                cartype = input("Type: ")
                carclass = input("Class: ")
                seats = input("How many seats: ")
                fwd = input("4x4 (Y/N): ").upper()
                transmission = input("Transmission: ")
                new_car = Car(id, model, cartype, carclass, seats, fwd, transmission)
                self.__car_service.add_car(new_car)

            elif action == "2":
                videos = self.__car_service.get_cars()
                print(videos)
