#  6. Напишите программу, которая открывает файл вывода number_list.txt,
#  но не стирает содержимое файла, если он уже существует.

def main():
    in_my_name = open('number_list.txt', 'a')
    number = input('number ')
    in_my_name.write(number + '\n')
    in_my_name.close()
    in_my_name = open('number_list.txt', 'r')
    for line in in_my_name:
        line = line.rstrip('\n')
        print(line)
    in_my_name.close()


main()
