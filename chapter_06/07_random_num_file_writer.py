#  7. Программа записи файла со случайными числами. Напишите программу,
#  которая пишет в файл ряд случайных чисел . Каждое случайное число должно
#  быть в диапазоне от 1 до 500. Приложение должно предоставлять пользователю
#  возможность назначать количество случайных чисел, которые будут
#  содержаться в файле.

import random


def main():
    count_num = int(input('Count numbers: '))
    open_file = open('numbers.txt', 'w')
    for num in range(count_num):
        open_file.write(str(random.randint(1, 500)) + '\n')
    open_file.close()


main()
