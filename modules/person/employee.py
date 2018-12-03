class Employee:
    __kt = None
    __id = None
    __f_name = None
    __l_name = None
    __email = None
    __phone_number = None

    def __init__(self, csv=None):
        csv_list = []
        if csv:
            csv_list = csv.strip().split(",")
        self.__kt = csv_list[0] if (len(csv_list) > 0) else ""
        self.__id = int(csv_list[1]) if (len(csv_list) > 1) else 0
        self.__f_name = csv_list[2] if (len(csv_list) > 2) else ""
        self.__l_name = csv_list[3] if (len(csv_list) > 3) else ""
        self.__email = csv_list[4] if (len(csv_list) > 4) else ""
        self.__phone_number = csv_list[5] if (len(csv_list) > 5) else ""

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

    def __str__(self):
        return "{},{},{},{},{},{}".format(
            self.__kt,
            self.__id,
            self.__f_name,
            self.__l_name,
            self.__email,
            self.__phone_number
        )

    def save(self, file):
        with open(file, "a") as myfile:
            myfile.write("{}\n".format(str(self)))


# les allar línur í skrá og bý til employee úr hverri línu


def read_file(file):
    employees = []
    with open(file, "r") as file:
        for line in file:
            line.strip()
            if len(line.strip()) > 0:
                employees.append(Employee(line))
    return employees


def print_all_employees(current_employees):
    for employee in current_employees:
        print(employee.get_id())
        print(employee.get_fname())
        print(employee.get_lname())
        print(employee.get_kt())
        print(employee.get_email())
        print(employee.get_phone_number())
        print("--------------------")

def create_new_employee(id):
    new_employee = Employee()
    new_name = input("Name: ")
    new_l_name = input("Last name: ")
    new_kt = int(input("kennitala: "))
    new_id = id
    new_email = input("Email: ")
    new_phone_number = input("Phone number: ")

    new_employee.set_f_name(new_name)
    new_employee.set_l_name(new_l_name)
    new_employee.set_kt(new_kt)
    new_employee.set_id(new_id)
    new_employee.set_email(new_email)
    new_employee.set_phone_number(new_phone_number)

    new_employee.save("../../data/employees.csv")


def main():
    current_employees = read_file("../../data/employees.csv")
    print_all_employees(current_employees)
    create_new_employee(len(current_employees) + 1)

main()
