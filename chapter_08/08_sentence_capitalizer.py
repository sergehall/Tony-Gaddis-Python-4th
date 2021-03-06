# sentence capitalizer#
# 8. Корректор предложений. Напишите программу с функцией, принимающей в
# качестве аргумента строковое значение и возвращающей его копию, в котором
# первый символ каждого предложения написан в верхнем регистре. Например,
# если аргументом является "привет! меня зовут джо. а как твое имя?", то эта
# функция должна вернуть строковое значение 'Привет! Меня зовут Джо. А как
# твое имя?'. Программа должна предоставить пользователю возможность ввести
# строковое значение и затем передать его в функцию. Модифицированное
# строковое значение должно быть выведено на экран.

# застрял с задачей на сутки!

def main():
    # my_string = input("Enter a string: ")
    my_string = "hello! mike, nina. my name is Bill. what're your names? " \
                "hello! mike. what's your names?"
    print()
    print(my_string)
    capitalizer_first_word(my_string)


def capitalizer_first_word(my_string):
    my_string2 = my_string.split()

    for i in range(0, len(my_string2)):
        if my_string2[i - 1].endswith('.') or my_string2[i - 1].endswith('!') \
                or my_string2[i - 1].endswith('?'):
            print(my_string2[i].capitalize(), end=' ')
        else:
            print(my_string2[i], end=' ')


main()
