class Order(object):
    def __init__(self, car='', renter='', FromDate="00/00/00", ToDate="00/00/00"):
        self.car = car
        self.renter = renter
        self.From_date = FromDate
        self.To_date = ToDate

    def get_car(self):
        return self.car

    def get_renter(self):
        return self.renter

    def get_from_date(self):
        return self.From_date

    def get_to_date(self):
        return self.To_date

    def set_car(self, other):
        self.car = other

    def set_renter(self, other):
        self.renter = other

    def set_from_date(self, other):
        self.From_date = other

    def set_to_date(self, other):
        self.To_date = other




