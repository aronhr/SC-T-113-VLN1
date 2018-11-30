from repositories.CarRepository import CarRepository


class CarService:
    def __init__(self):
        self.__car_repo = CarRepository()

    def add_car(self, video):
        if self.is_valid_car(video):
            self.__car_repo.add_car(video)

    def is_valid_car(self, car):
        # here should be some code to
        # validate the video
        return True

    def get_cars(self):
        return self.__car_repo.get_car()

    def get_videos_by_genre(self, genre):
        pass
