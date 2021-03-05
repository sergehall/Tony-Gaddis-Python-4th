# 2. Напишите программу, которая открывает файл my_name.txt,
# созданный программой в задаче  читает
# ваше имя из файла, выводит имя на экран и затем закрывает файл.

def main():
    in_my_name = open('my_name.txt', 'r')
    for line in in_my_name:
        print(line)
    in_my_name.close()


main()
