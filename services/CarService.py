from repositories.CarRepository import CarRepository
import datetime
import string


class CarService:
    def __init__(self):
        self.__car_repo = CarRepository()

    def add_car(self, car):
        self.__car_repo.add_car(car)

    def get_cars(self):
        return self.__car_repo.get_car()

    def get_car_by_license(self, license):
        car = self.get_cars()
        for x in car:
            if x["License"] == license:
                return x
        else:
            return False

    @staticmethod
    def next_list(stop):
        start = stop
        stop = start * 2
        return start, stop, start + 1
    
    @staticmethod
    def prev_list(start):
        stop = start
        start = stop - 10
        return start, stop, start + 1

    def get_cars_by_type(self, type):
        cars = self.get_available_cars()
        arr = []
        for x in cars:
            if x["Class"] == type:
                arr.append(x)
        return arr

    def get_car_class(self):
        cars = self.get_available_cars()
        if cars:
            arr = []
            for x in cars:
                if x["Class"] not in arr:
                    arr.append(x["Class"])
            return arr
        else:
            return False

    def get_available_cars(self):
        return self.__car_repo.get_available_car("True")

    def get_not_available_cars(self):
        return self.__car_repo.get_available_car("False")

    def user_date(self, i):
        is_valid = False
        while not is_valid:
            user_in = input(i).lower().replace(string.punctuation,  "")
            try:
                d = datetime.datetime.strptime(user_in, "%d/%m/%y")
                yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
                if d >= yesterday:
                    is_valid = True
                else:
                    print("Time traveling?")
            except Exception:
                print("Wrong date, try again")
        return d

    def get_available_date_cars(self, from_date, to_date):
        available_cars = self.__car_repo.get_available_date_car(from_date, to_date)
        car = self.get_available_cars()
        cars = []
        # Cars that are unavailable
        try:
            for x in car:
                for y in available_cars:
                    if x["License"] != y["License"]:
                        cars.append(x)
            if not cars:
                for x in car:
                    cars.append(x)
            return cars
        except Exception:
            return car

    def get_available_date_type(self, genre, from_date, to_date):
        cars = self.get_available_date_cars(from_date, to_date)
        if cars:
            arr = []
            for x in cars:
                if x["Class"] == genre:
                    arr.append(x)
            return arr
        else:
            return False

    def get_car_by_id(self, id):
        return self.__car_repo.get_car_id(id-1)

    def remove_car(self, id):
        return self.__car_repo.remove_car_id(id)

    @staticmethod
    def check_car_class(i, e):
        c_class = ""
        while c_class == "":
            car_class = input(i).lower()
            if car_class.isdigit():
                if car_class == "1":
                    c_class = "Luxury"
                elif car_class == "2":
                    c_class = "Sport"
                elif car_class == "3":
                    c_class = "Off-road"
                elif car_class == "4":
                    c_class = "Sedan"
                elif car_class == "5":
                    c_class = "Economy"
                elif car_class == "q":
                    break
                else:
                    print(e)
            else:
                print(e)
        return c_class

    @staticmethod
    def transmission(i, e):
        while True:
            transmission = input(i).upper()
            if transmission == "A" or transmission == "M":
                break
            else:
                print(e)
        return transmission
