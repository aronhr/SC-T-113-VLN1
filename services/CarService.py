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
        """
        this takes care of if the list is enormous, this function will take care of that.
        :param stop:
        :return:
        """
        start = stop
        stop = start + 10
        return start, stop, start + 1

    @staticmethod
    def prev_list(start):
        """
        This we go back in the enormous list
        :param start:
        :return:
        """
        stop = start
        start = stop - 10
        return start, stop, start + 1

    def get_cars_by_type(self, type):
        """
        Gets car the by the type that the user want to see
        :param type:
        :return:
        """
        cars = self.get_available_cars()
        arr = []
        for x in cars:
            if x["Class"] == type:
                arr.append(x)
        return arr

    def get_car_class(self):
        """
        Gets car by the class that the user want to see
        :return:
        """
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
        """
        Calls the get_available_car and uses it here, and leave you with "true"
        :return:
        """
        return self.__car_repo.get_available_car("True")

    def get_not_available_cars(self):
        """
        Calls the get_available_car and uses it here, and leave you with "False"
        :return:
        """
        return self.__car_repo.get_available_car("False")

    def user_date(self, i):
        """
        Checks if the date is valid or not.
        :param i:
        :return:
        """
        is_valid = False
        while not is_valid:
            user_in = input(i).replace(string.punctuation,  "")
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
        """
        gets the available cars the available date
        :param from_date:
        :param to_date:
        :return:
        """
        available_cars = self.__car_repo.get_available_date_car(from_date, to_date)
        car = self.get_available_cars()
        cars = []
        # Cars that are unavailable
        try:
            for x in car:
                for y in available_cars:
                    if x["License"] == y["License"]:
                        cars.append(x)
                        break
            if not cars:
                for x in car:
                    cars.append(x)
            return cars
        except Exception:
            return car

    def get_available_date_type(self, genre, from_date, to_date):
        """
        Gets available type with available date.
        :param genre:
        :param from_date:
        :param to_date:
        :return:
        """
        cars = self.get_available_date_cars(from_date, to_date)
        all_cars = self.get_available_cars()
        if cars:
            arr = []
            for x in all_cars:
                if x["Class"] == genre:
                    if x not in cars:
                        arr.append(x)
            if not arr:
                for x in all_cars:
                    if x["Class"] == genre:
                        arr.append(x)
            return arr
        else:
            return False

    def get_car_by_id(self, id, stat="All"):
        """
        Call the function get car id to get the specific car.
        :param id:
        :return:
        """
        return self.__car_repo.get_car_id(id - 1, stat)

    def remove_car(self, id):
        """
        Calls the remove car id function to remove the specific car.
        :param id:
        :return:
        """
        return self.__car_repo.remove_car_id(id)

    @staticmethod
    def check_car_class(i, e):
        """
        Shows all types of cars that we have to offer, and asks to pick a class
        :param i:
        :param e:
        :return:
        """
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
        """
        Checks if the transmission is valid or not
        :param i:
        :param e:
        :return:
        """
        while True:
            transmission = input(i).upper()
            if transmission == "A" or transmission == "M":
                break
            else:
                print(e)
        return transmission
