class Customer(object):
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__kt = ""
        self.__country = ""
        self.__address = ""
        self.__mail = ""
        self.__phone_number = ""
        self.__license = ""
        self.__age = 0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_kt(self):
        return self.__kt

    def get_country(self):
        return self.__country

    def get_address(self):
        return self.__address

    def get_mail(self):
        return self.__mail

    def get_phone_number(self):
        return self.__phone_number

    def get_license(self):
        return self.__license

    def get_age(self):
        return self.__age

    def set_id(self, other):
        self.__id = other

    def set_name(self, other):
        self.__name = other

    def set_kt(self, other):
        self.__kt = other

    def set_country(self, other):
        self.__country = other

    def set_address(self, other):
        self.__address = other

    def set_mail(self, other):
        self.__mail = other

    def set_phone_number(self, other):
        self.__phone_number = other

    def set_license(self, other):
        self.__license = other

    def set_age(self, other):
        self.__age = other