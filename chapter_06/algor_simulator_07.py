#  7. На диске существует файл students. txt. Он содержит несколько
#  записей, и каждая запись имеет два поля: имя студента и оценку студента за
#  итоговый экзамен. Напишите программу, которая удаляет запись с именем
#  студента "Джон Перц". программа для создания файла  students. txt

import os


def main():
    found = False
    search = input('Кого будем удалять? ')
    students_file = open('students.txt', 'r')
    temp_students_file = open('temp.txt', 'w')
    student = students_file.readline()
    while student != '':
        score = int(students_file.readline())
        student = student.rstrip('\n')
        if student != search:
            temp_students_file.write(student + '\n')
            temp_students_file.write(str(score) + '\n')
        else:
            found = True
        student = students_file.readline()
    students_file.close()
    temp_students_file.close()
    os.remove('students.txt')
    os.rename('temp.txt', 'students.txt')
    # Если искомое значение в файле не найдено,  то показать сообщение.
    if found:
        print('File upgraded')
    else:
        print('File not found')


main()
