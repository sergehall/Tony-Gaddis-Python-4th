#  12. В файле имеется 365 строк, и каждая строка содержит количество шагов,
#  сделанных в течение дня. Напишите программу, которая читает файл и затем
#  выводит среднее количество шагов, сделанных в течение каждого месяца. (
#  Данные были записаны в год, который не был високосным, и поэтому февраль
#  имеет 28 дней.) Создал 365 строк с рандомным количеством шагов.

import random


def main():
    open_file = open('steps.txt', 'w')
    DAYS_YEAR = 365
    for line in range(DAYS_YEAR):
        open_file.write(str(random.randint(9000, 12000)) + '\n')
    open_file.close()

    def count_steps():
        days = 2
        open_file = open('steps.txt', 'r')
        content = open_file.readline()

        total_jan = 0
        total_feb = 0
        total_mar = 0
        total_apr = 0
        total_may = 0
        total_jun = 0
        total_jul = 0
        total_aug = 0
        total_sep = 0
        total_oct = 0
        total_nov = 0
        total_dec = 0
        while content != '':
            if days <= 32:
                content = content.rstrip('\n')
                total_jan += int(content)
                days += 1
            if 32 < days <= 60:
                content = content.rstrip('\n')
                total_feb += int(content)
                days += 1
            if 60 < days <= 90:
                content = content.rstrip('\n')
                total_mar += int(content)
                days += 1
            if 90 < days <= 121:
                content = content.rstrip('\n')
                total_apr += int(content)
                days += 1
            if 121 < days <= 151:
                content = content.rstrip('\n')
                total_may += int(content)
                days += 1
            if 151 < days <= 182:
                content = content.rstrip('\n')
                total_jun += int(content)
                days += 1
            if 182 < days <= 212:
                content = content.rstrip('\n')
                total_jul += int(content)
                days += 1
            if 212 < days <= 243:
                content = content.rstrip('\n')
                total_aug += int(content)
                days += 1
            if 243 < days <= 273:
                content = content.rstrip('\n')
                total_sep += int(content)
                days += 1
            if 273 < days <= 304:
                content = content.rstrip('\n')
                total_oct += int(content)
                days += 1
            if 304 < days <= 334:
                content = content.rstrip('\n')
                total_nov += int(content)
                days += 1
            if 334 < days <= 365:
                content = content.rstrip('\n')
                total_dec += int(content)
                days += 1

            content = open_file.readline()
        print('Jan: ', total_jan)
        print('Feb: ', total_feb)
        print('Mar: ', total_mar)
        print('Apr: ', total_apr)
        print('May: ', total_may)
        print('Jun: ', total_jun)
        print('Jul: ', total_jul)
        print('Aug: ', total_aug)
        print('Sep: ', total_sep)
        print('Oct: ', total_oct)
        print('Nov: ', total_nov)
        print('Dec: ', total_dec)
        open_file.close()

    count_steps()


main()
