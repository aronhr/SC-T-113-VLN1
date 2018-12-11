class Order(object):
    def __init__(self, kt='', renter='', car='', FromDate="", ToDate="", price=0, insurance="N", price_insurance=0, days=0, payment_method=''):
        if insurance == "N":
            insurance = "No"
        elif insurance == "No":
            pass
        elif insurance == "Y":
            insurance = "Yes"
        elif insurance == "Yes":
            pass

        self.__kt = kt
        self.__car = car
        self.__renter = renter
        self.__From_date = FromDate
        self.__To_date = ToDate
        self.__price = price
        self.__payment_method = payment_method
        self.__insurance = insurance
        self.__price_insurance = price_insurance
        self.__days = days

    def get_insurance(self):
        return self.__insurance

    def get_price_insurance(self):
        return self.__price_insurance

    def get_days(self):
        return self.__days

    def get_kt(self):
        return self.__kt

    def get_car(self):
        return self.__car

    def get_renter(self):
        return self.__renter

    def get_from_date(self):
        return self.__From_date

    def get_to_date(self):
        return self.__To_date

    def get_price(self):
        return self.__price

    def get_payment_method(self):
        return self.__payment_method

    def set_insurance(self, other):
        self.__insurance = other

    def set_price_insurance(self, other):
        self.__price_insurance = other

    def set_days(self, other):
        self.__days = other

    def set_kt(self, other):
        self.__kt = other

    def set_car(self, other):
        self.__car = other

    def set_renter(self, other):
        self.__renter = other

    def set_from_date(self, other):
        self.__From_date = other

    def set_to_date(self, other):
        self.__To_date = other

    def set_price(self, other):
        self.__price = other

    def set_payment_method(self, other):
        self.__payment_method = other

    def __repr__(self):
        return "{},{},{},{},{},{},{}".format(self.get_kt(), self.get_renter(), self.get_car(), self.get_from_date(), self.get_to_date(), self.get_price(), self.get_payment_method())



