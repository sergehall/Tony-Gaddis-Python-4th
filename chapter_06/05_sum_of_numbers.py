#  5. Сумма чисел. Допустим, что файл с рядом целых чисел называется
#  numbers .txt и существует на диске компьютера. Напишите программу, которая
#  читает все хранящиеся в файле числа и вычисляет их сумму. number_list.txt


def main():
    try:
        name_file = input('Name file + .file extension: ')
        open_file = open(str(name_file), 'r')
        total = 0
        for content in open_file:
            content = int(content.rstrip('\n'))

            total += content
        print(total)

    except ValueError:
        print('ValueError')
    except FileNotFoundError:
        print('FileNotFoundError')


main()