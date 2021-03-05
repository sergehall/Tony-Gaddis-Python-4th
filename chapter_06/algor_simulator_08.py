#  8. На диске существует файл students.txt. Он содержит несколько записей,
#  и каждая запись имеет два поля: имя студента и оценку студента за итоговый
#  экзамен. Напишите программу, которая меняет оценку Джулии Милан на 100.

import os


def main():
    found = False
    search = input('Кому меняем score ? ')
    new_score = int(input('New score: '))
    students_file = open('students.txt', 'r')
    temp_file = open('temp.txt', 'w')
    students = students_file.readline()
    while students != '':
        score = int(students_file.readline())
        students = students.rstrip('\n')
        # Записать во временный файл либо эту запись, либо новую запись,
        # если эта запись подлежит изменению.
        if students == search:
            temp_file.write(students + '\n')
            temp_file.write(str(new_score) + '\n')
            # Назначить флагу found значение True.
            found = True
        else:
            # Записать исходную запись во временный файл.
            temp_file.write(students + '\n')
            temp_file.write(str(score) + '\n')
        students = students_file.readline()
    students_file.close()
    temp_file.close()
    # Удалить исходный файл coffee.txt.
    os.remove('students.txt')
    # Переименовать временный файл.
    os.rename('temp.txt', 'students.txt')
    # Если искомое значение в файле не найдено, то показать сообщение.
    if found:
        print('File upgraded')
    else:
        print('Такого имени не найдено.')


main()
