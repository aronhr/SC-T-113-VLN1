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

    def get_cars_by_type(self, genre):
        cars = self.get_available_cars()
        arr = []
        for x in cars:
            if x["Class"] == genre:
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
            user_in = input(i).replace(string.punctuation, "")
            try:
                d = datetime.datetime.strptime(user_in, "%d/%m/%y")
                if d >= datetime.datetime.today():
                    is_valid = True
                else:
                    print("Time traveling?")
            except Exception:
                print("Wrong date, try again")
        return d

    def get_available_date_cars(self, from_date, to_date):
        available_cars = self.__car_repo.get_available_date_car(from_date, to_date)
        car = self.__car_repo.get_car()
        cars = []
        # Cars that are unavailable
        try:
            for x in car:
                for y in available_cars:
                    if x["License"] == y["License"]:
                        pass
                    else:
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
