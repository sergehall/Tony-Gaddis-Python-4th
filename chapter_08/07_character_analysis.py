# 7. Анализ символов. Среди исходного кода главы 8, а также в подпапке
# data "Решений задач по программированию" соответствующей главы вы найдете
# файл text.txt. Напишите программу, которая читает содержимое файла и
# определяет: 1) количество букв в файле в верхнем регистре. 2) количество
# букв в файле в нижнем регистре. 3) количество цифр в файле.
# 4) количество  пробельных символов в файле.


def count():
    open_file_read = open('text.txt', 'r')
    content = open_file_read.readlines()  # по одной строке считываем из файла
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_whitespace = 0

    for string in content:
        for ch in string:
            # print(ch)
            if ch.isalpha():
                if ch == ch.upper():
                    count_upper += 1
                if ch == ch.lower():
                    count_lower += 1
            if ch.isdigit():
                count_digit += 1
            if ch.isspace():
                count_whitespace += 1
    open_file_read.close()

    print('The number of uppercase letters in the file is = ', count_upper)
    print('The number of lowercase letters in the file is = ', count_lower)
    print('The number of digits in the file is = ', count_digit)
    print('The number of whitespace characters in the file'
          ' is = ', count_whitespace)


count()
