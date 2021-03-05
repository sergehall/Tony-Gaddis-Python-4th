# 4. Напишите программу, которая делает следующее: открывает файл
# number_list.txt, созданный программой, которую вы написали в задаче 3,
# читает все числа из файла, выводит их на экран и затем закрывает файл.

def main():
    in_my_name = open('number_list.txt', 'r')
    for contents in in_my_name:
        contents = contents.rstrip('\n')
        print(contents)
    in_my_name.close()


main()
