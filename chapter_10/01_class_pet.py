class Pet:

    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_publisher_name(self, age):
        self.__age = age

    def __str__(self):
        return "Name: " + self.__name + "\n" \
               + "Animal type: " + self.__animal_type + "\n" \
               + "Age: " + str(self.__age)


def main():
    # в ручную ввели
    my_pet = Pet("Bobbik", "Dog", 7)
    print(my_pet)

    # с помощью цикла выводим данные одращаясь к обьекту класса используя
    # методы класса

    print(my_pet.get_name())
    print(my_pet.get_animal_type())
    print(my_pet.get_age())


main()