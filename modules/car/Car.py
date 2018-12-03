class Car(object):
    def __init__(self, model="", cartype="", carclass="", seats=0, fwd="", transmission=""):
        if fwd == "Y":
            fwd = "Yes"
        else:
            fwd = "No"

        if transmission == "A":
            transmission = "Automatic"
        elif transmission == "M":
            transmission = "Manual"
        elif transmission == "Automatic":
            pass
        elif transmission == "Manual":
            pass
        else:
            transmission = "Something new?"

        self.__id = 0
        self.__model = model
        self.__type = cartype
        self.__class = carclass
        self.__seats = seats
        self.__4x4 = fwd
        self.__transmission = transmission

        price = 500
        price += 500*(seats/10)  # Bíll kostar 500 kr. á dag margfaldað með 1,fjöldi_sæta
        if self.__class == "Luxury":
            price = price*1.5
        if self.__4x4 is True:
            price = price*1.2
        if self.__transmission == "Automatic":
            price = price*1.1

        self.__price = price

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

    def get_price(self):
        return self.__price

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
        if other == "Y":
            other = "Yes"
        else:
            other = "No"
        self.__4x4 = other

    def set_transmission(self, transmission):
        if transmission == "A":
            transmission = "Automatic"
        elif transmission == "M":
            transmission = "Manual"
        elif transmission == "Automatic":
            pass
        elif transmission == "Manual":
            pass
        else:
            transmission = "Something new?"
        self.__transmission = transmission

    def set_price(self, other):
        self.__price = other

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.get_model(), self.get_type(), self.get_class(), self.get_seats(),
                                             self.get_4x4(), self.get_transmission(), self.get_price())
