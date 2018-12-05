class Employee:

    def __init__(self, kt="", id=0, fname="",lname="",email="",phonenumber=0):
        self.__kt = kt.replace("-", "").replace(" ", "")
        self.__id = id
        self.__f_name = fname
        self.__l_name = lname
        self.__email = email
        self.__phone_number = phonenumber

    def get_kt(self):
        return self.__kt

    def get_id(self):
        return self.__id

    def get_fname(self):
        return self.__f_name

    def get_lname(self):
        return self.__l_name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def set_kt(self, other):
        self.__kt = other

    def set_id(self, other):
        self.__id = other

    def set_f_name(self, other):
        self.__f_name = other

    def set_l_name(self, other):
        self.__l_name = other

    def set_email(self, other):
        self.__email = other

    def set_phone_number(self, other):
        self.__phone_number = other

