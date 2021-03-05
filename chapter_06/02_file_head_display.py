# 2. Вывод на экран верхней части файла. Напишите программу, которая
# запрашивает у пользователя имя файла. Программа должна вывести на экран
# только первые пять строк содержимого файла. Если в файле меньше пяти строк,
# то она должна вывести на экран все содержимое файла. number_list.txt

def main():
    try:
        name_file = input('Name file + .file extension: ')
        num_str = int(input('Num str: '))
        open_file = open(str(name_file), 'r')
        for content in open_file:
            if num_str > 0:
                print(content)
            num_str -= 1
        open_file.close()

    except ValueError:
        print('ValueError')
    except FileNotFoundError:
        print('FileNotFoundError')


main()
