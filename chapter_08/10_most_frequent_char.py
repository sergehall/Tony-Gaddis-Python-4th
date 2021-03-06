# most frequent character
# 10. Самый частотный символ. Напишите программу, которая предоставляет
# пользователю возможность ввести строковое значение и выводит на экран
# символ, который появляется в нем наиболее часто.

from collections import Counter


def main():
    # user_string = input("Enter a string: ")
    my_string = "hello! mike. nina. my name is Bill. what's your name?"
    # возращает список в в списке с 3 мах частыми символами
    max_3 = Counter(my_string).most_common(3)
    print("The most frequently occuring letter is", max_3)


main()