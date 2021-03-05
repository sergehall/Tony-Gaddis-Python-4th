# 2. Генератор лотерейных чисел. Разработайте программу, которая генерирует
# семизначную комбинацию лотерейных чисел. Программа должна сгенерировать
# семь случайных чисел, каждое в диапазоне от О до 9, и присвоить каждое
# число элементу списка. (Случайные числа рассматривались в главе 5.) Затем
# напишите еще один цикл, который показывает содержимое списка.

from random import randint


def main():
    numbers_in_ticket = int(input('Numbers_in_ticket: '))
    number = []
    for i in range(numbers_in_ticket):
        number.append(randint(0, 9))
    print(number)


main()

# lottery number generator

# import random
#
#
# def main():
#     numbers = random_number_generator()
#
#     print("The lucky numbers are below. Thanks for participating.")
#     print()
#     index = 0
#     while index < len(numbers):
#         print(numbers[index], end="  ")
#         index += 1
#
#
# def random_number_generator():
#     # create an empty list
#     numbers = []
#
#     # we can just use append (it will iterate 7 times)
#     for i in range(7):
#         numbers.append(random.randrange(0, 10))
#     return numbers
#
#
# # call the main function
# main()