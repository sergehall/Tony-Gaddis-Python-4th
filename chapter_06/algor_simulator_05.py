# 5. Измените программу, которую вы написали в задаче 4 таким образом,
# чтобы она суммировала все прочитанные из файла числа и выводила на экран их
# сумму.

def main():
    in_my_name = open('number_list.txt', 'r')
    total = 0
    contents = in_my_name.readline()
    while contents != '':
        amount = int(contents)
        total += amount
        contents = in_my_name.readline()
    in_my_name.close()
    print(total)


main()
