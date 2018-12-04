from repositories.CarRepository import CarRepository


class CarService:
    def __init__(self):
        self.__car_repo = CarRepository()

    def add_car(self, car):
        if self.is_valid_car(car):
            self.__car_repo.add_car(car)

    @staticmethod
    def is_valid_car(car):
        # here should be some code to
        # validate the car
        return True

    def get_cars(self):
        return self.__car_repo.get_car()

    def get_cars_by_type(self, genre):
        cars = self.get_available_cars()
        arr = []
        for x in cars:
            if x["Class"] == genre:
                arr.append(x)
        return arr

    def get_available_cars(self):
        return self.__car_repo.get_available_car("True")

    def get_not_available_cars(self):
        return self.__car_repo.get_available_car("False")

    def get_available_date_cars(self, from_date, to_date):
        return self.__car_repo.get_available_date_car(from_date, to_date)

    def get_car_by_id(self, id):
        return self.__car_repo.get_car_id(id-1)

    def remove_car(self, id):
        return self.__car_repo.remove_car_id(id)
