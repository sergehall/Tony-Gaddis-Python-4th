# 6. Среднее арифметическое чисел. Допустим, что файл с рядом целых
# чис~л называется numbers.txt и существует на диске компьютера. Напишите
# программу, которая вычисляет среднее арифметическое всех хранящихся в файле
# чисел. number_list.txt

def main():
    try:
        name_file = input('Name file + .file extension: ')
        open_file = open(str(name_file), 'r')
        total = 0
        count = 0
        for content in open_file:
            content = int(content.rstrip('\n'))
            count += 1
            total += content
        print(total, ', ', count, ', ',
              'Среднее арифметическое = ', total // count, sep='')



    except ValueError:
        print('ValueError')
    except FileNotFoundError:
        print('FileNotFoundError')


main()
