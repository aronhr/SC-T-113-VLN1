class Car(object):
    def __init__(self, model="", cartype="", carclass="", seats=0, fwd="", transmission="", license="", price=500, status="True"):
        if fwd == "Y":
            fwd = "Yes"
        elif fwd == "Yes":
            pass
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

        if status == "T":
            status = "True"
        elif status == "F":
            status = "False"
        elif status == "True":
            pass
        elif status == "False":
            pass
        else:
            status = "True"

        self.__id = 0
        self.__model = model
        self.__type = cartype
        self.__class = carclass
        self.__seats = seats
        self.__4x4 = fwd
        self.__transmission = transmission
        self.__price = self.set_price()
        self.__status = status
        self.__license = license

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

    def get_status(self):
        return self.__status

    def get_license(self):
        return self.__license

    def set_license(self, other):
        self.__license = other

    def set_price(self):
        if self.__class == "Luxury":
            self.__price = 8500
        elif self.__class == "Sport" or "Sports":
            self.__price = 7500
        elif self.__class == "Off-Road" or "Off-Roader":
            self.__price = 7000
        elif self.__class == "Sedan":
            self.__price = 5500
        elif self.__class == "Economy":
            self.__price = 4000
        else:
            self.__price = 5000
        return self.__price

    def set_id(self, other):
        self.__id = other

    def set_model(self, other):
        self.__model = other

    def set_type(self, other):
        self.__type = other

    def set_class(self, other):
        self.__class = other
        self.set_price()

    def set_seats(self, other):
        self.__seats = other
        self.set_price()

    def set_4x4(self, other):
        if other == "Y":
            other = "Yes"
        else:
            other = "No"
        self.__4x4 = other
        self.set_price()

    def set_transmission(self, transmission):
        if transmission == "A":
            transmission = "Automatic"
        elif transmission == "M":
            transmission = "Manual"
        else:
            transmission = "Something new?"
        self.__transmission = transmission
        self.set_price()

    def set_status(self, status):
        if status == "T":
            status = "True"
        elif status == "F":
            status = "False"
        elif status == "True":
            pass
        elif status == "False":
            pass
        else:
            status = "True"
        self.__status = status

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.get_model(), self.get_type(), self.get_class(), self.get_seats(),
                                             self.get_4x4(), self.get_transmission(), self.get_price())
