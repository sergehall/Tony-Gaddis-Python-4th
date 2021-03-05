# 5. Проверка допустимости номера расходноrо счета. Среди исходного
# кода главы 7, а также в подпапке data "Решений задач по программированию"
# соответствующей главы вы найдете файл charge_accounts.txt. Этот файл
# содержит список допустимых номеров расходных счетов компании. Каждый номер
# счета представляет собой семизначное число, в частности 5658845. Напишите
# программу, которая считывает содержимое файла в список. Затем эта программа
# должна попросить пользователя ввести номер расходного счета. Программа
# должна определить, что номер является допустимым, путем его поиска в списке.
# Если число в списке имеется, то программа должна вывести сообщение,
# указывающее на то, что номер допустимый. Если числа в списке нет,
# то программа должна вывести сообщение, указывающее на то, что номер
# недопустимый.

import random


def main():
    # создаю файл charge_accounts.txt со списком счетов внутри
    list_numbers = [random.randint(1000000, 9999999) for num in range(10)]
    charge_accounts_list = open('charge_accounts.txt', 'w')
    for i in list_numbers:
        creat_account_number = charge_accounts_list.write(str(i) + '\n')
    charge_accounts_list.close()

    # инструкция для открытия файла и считывание его в список
    # charge_accounts.txt и удаление в каждой строке '\n'
    list_numbers_read = open('charge_accounts.txt', 'r')
    numbers_str_list = list_numbers_read.readlines()
    list_numbers_read.close()

    index = 0
    while index < len(numbers_str_list):
        numbers_str_list[index] = numbers_str_list[index].rstrip('\n')
        index += 1
    print(numbers_str_list)
    # вводим свой номер и проверяем есть ли он в списке
    num_account = input("Please enter the charge account number:\n")
    if num_account in numbers_str_list:
        print('The number', num_account, 'is valid.')
    else:
        print("ERROR: The number", num_account, "is NOT valid.\n"
                                                "It is not found in the file"
                                                " 'charge_accounts.txt.'")


main()
