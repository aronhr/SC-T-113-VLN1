class Car(object):
    def __init__(self, model="", cartype="", carclass="", seats=0, fwd=None, transmission=""):
        if fwd == "Y":
            self.__4x4 = True
        else:
            self.__4x4 = False

        self.__id = 0
        self.__model = model
        self.__type = cartype
        self.__class = carclass
        self.__seats = seats
        self.__4x4 = fwd
        self.__transmission = transmission

    def get_id(self):
        return self.__id

    def get_model(self):
        return self.__model

    def get_type(self):
        return self.__type

    def get_class(self):
        return self.__class

    def get_seats(self):
        return self.__seats

    def get_4x4(self):
        return self.__4x4

    def get_transmission(self):
        return self.__transmission

    def set_id(self, other):
        self.__id = other

    def set_model(self, other):
        self.__model = other

    def set_type(self, other):
        self.__type = other

    def set_class(self, other):
        self.__class = other
        
    def set_seats(self, other):
        self.__seats = other

    def set_4x4(self, other):
        self.__4x4 = other

    def set_transmission(self, other):
        self.__transmission = other


