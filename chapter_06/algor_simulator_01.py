# 2. Напишите программу, которая открывает файл my_name.txt,
# созданный программой в задаче  читает
# ваше имя из файла, выводит имя на экран и затем закрывает файл.

def main():
    name = input('My name ')
    my_name = open('my_name.txt', 'w')
    my_name.write(name + '\n')
    my_name.close()


main()
