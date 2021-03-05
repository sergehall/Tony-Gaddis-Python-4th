#  4. Счетчик значений. Допустим, что файл с серией имен
#  (в виде строковых значений) называется my_name.txt и существует на диске
#  компьютера. Напишите программу, которая показывает количество хранящихся в
#  файле имен. (Подсказка: откройте файл и прочитайте каждую хранящуюся в нем
#  строку . Примените переменную для подсчета количества прочитанных из файла
#  значений.)

def main():
    try:
        name_file = input('Name file + .file extension: ')
        open_file = open(str(name_file), 'r')
        total = 0
        for content in open_file:
            total += 1
        print(total)

    except ValueError:
        print('ValueError')
    except FileNotFoundError:
        print('FileNotFoundError')


main()
