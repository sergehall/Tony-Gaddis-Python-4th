# personal Information class

class Information:

    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    # create a method for showing object's state
    def __str__(self):
        return self.__name + ", " + \
               self.__address + ", " + \
               str(self.__age) + ", " + \
               self.__phone


my_info = Information("Serge", "Los Angeles", 38, "333-5555")
my_friend1 = Information("Vova", "New York", 35, "555-1111")
my_friend2 = Information("Lika", "Los Angeles", 28, "111-9999")

print("You have created three instances of the class Informaishion.")
print("object(name, address, age, phone)")
print("my_info(", my_info, ")", sep='')
print("my_friend1(", my_friend1, ")", sep='')
print("my_friend2(", my_friend2, ")", sep='')
