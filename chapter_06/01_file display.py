#  1. Вывод файла на экран. Допустим, что файл numbers.txt содержит ряд
#  целых чисел и существует на диске компьютера. Напишите программу, которая
#  выводит на экран все числа в файле.

def main():
    open_file = open('number_list.txt', 'r')
    for contents in open_file:
        contents = contents.rstrip('\n')
        print(contents)
    open_file.close()


main()