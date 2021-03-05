# 3. Напишите программу, которая делает следующее: открывает
# выходной файл с именем number_list.txt, применяет цикл для записи в файл
# чисел с 1 по 100, а затем закрывает файл.

def main():
    in_my_name = open('number_list.txt', 'w')
    for line in range(1, 101):
        in_my_name.write(str(line) + '\n')
    in_my_name.close()


main()
