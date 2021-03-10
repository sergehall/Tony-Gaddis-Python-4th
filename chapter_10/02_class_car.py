class Car:

    def __init__(self, year, make):
        self.__year = year
        self.__make = make
        self.__speed = 0

    def speed_car(self):
        return self.__speed

    def accelerate_car(self):
        self.__speed += 5
        return self.__speed

    def break_car(self):
        self.__speed -= 5
        return self.__speed

    def __str__(self):
        return self.__make + " " + self.__year + "\n" \
               + "Current speed: " + str(self.__speed)


def main():
    my_car = Car("2016", "Toyota")
    for i in range(5):
        my_car.accelerate_car()
        print("current speed: ", my_car.speed_car())

    print()

    for i in range(5):
        my_car.break_car()
        print("current speed: ", my_car.speed_car())

    print()
    print(my_car)


main()