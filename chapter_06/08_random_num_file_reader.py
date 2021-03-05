#  8. Программа чтения файлов со случайными числами. Выполнив предыдущее
#  задание (программу записи файла со случайными числами), напишите еще одну
#  программу, которая читает случайные числа из файла, выводит их на экран и
#  затем показывает приведенные ниже данные: 1) сумму чисел; 2) количество
#  случайных чисел, прочитанных из файла.

import random


def main():
    count_num = int((random.randint(1, 500)))
    open_file = open('numbers.txt', 'w')
    count = 0
    total = 0
    for num in range(count_num):
        open_file.write(str(random.randint(1, 500)) + '\n')
    open_file.close()
    open_file = open('numbers.txt', 'r')
    for num in open_file:
        num = int(num.rstrip('\n'))
        total += num
        count += 1
    print('Count: ', count, '\n', 'Total sum: ', total, sep='')


main()