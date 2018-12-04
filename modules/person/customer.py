from modules.person.Person import Person


class Customer(Person):
    def __init__(self, name='', kt='', country='', address='', mail='', phone='', d_license='', age=0):
        Person.__init__(self, name, kt, country, address, mail, phone, d_license, age)
