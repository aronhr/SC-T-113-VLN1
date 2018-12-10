class Order(object):
    def __init__(self, renter='', car='', FromDate="", ToDate="", price=0, payment_method=''):
        self.car = car
        self.renter = renter
        self.From_date = FromDate
        self.To_date = ToDate
        self.price = price
        self.payment_method = payment_method

    def get_car(self):
        return self.car

    def get_renter(self):
        return self.renter

    def get_from_date(self):
        return self.From_date

    def get_to_date(self):
        return self.To_date

    def get_price(self):
        return self.price

    def get_payment_method(self):
        return self.payment_method

    def set_car(self, other):
        self.car = other

    def set_renter(self, other):
        self.renter = other

    def set_from_date(self, other):
        self.From_date = other

    def set_to_date(self, other):
        self.To_date = other

    def set_price(self, other):
        self.price = other

    def set_payment_method(self, other):
        self.payment_method = other

    def __repr__(self):
        return "{},{},{},{},{}".format(self.car, self.renter, self.From_date, self.To_date, self.price)



