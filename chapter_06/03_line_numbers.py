#  3. Номера строк. Напишите программу, которая запрашивает у пользователя
#  имя файла. Программа должна вывести на экран содержимое файла, при этом
#  каждая строка должна предваряться ее номером и двоеточием. Нумерация строк
#  должна начинаться с 1. number_list.txt

def main():
    try:
        name_file = input('Name file + .file extension: ')
        open_file = open(str(name_file), 'r')
        count = 1
        for content in open_file:
            content = content.rstrip('\n')
            print(count, ': ', content, sep='')
            count += 1
        open_file.close()

    except ValueError:
        print('ValueError')
    except FileNotFoundError:
        print('FileNotFoundError')


main()
