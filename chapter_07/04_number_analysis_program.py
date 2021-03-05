# 4. Проrрамма анализа чисел. Разработайте программу, которая просит
# пользователя ввести ряд из 20 чисел. Программа должна сохранить числа в
# списке и затем показать приведенные ниже данные:

import random


def main():
    twenty_numbers, total, average = get_numbers()
    print(twenty_numbers)
    print("The lowest number in this list is", min(twenty_numbers))
    print("The maximum number in this list is", max(twenty_numbers))
    print("The total of numbers is", total)
    print("The average of numbers is", average)


def get_numbers():
    twenty_numbers = [random.randint(-100, 1000) for i in range(20)]
    total = 0
    for num in twenty_numbers:
        total += num
    average = total // len(twenty_numbers)
    return twenty_numbers, total, average


main()
