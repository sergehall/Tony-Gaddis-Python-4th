# time calculator
# Калькулятор времени. Напишите программу, которая просит пользователя ввести
# количество секунд получаем года, месеца, дни, мин, сек

# ask user to enter a number of seconds

t_sec = int(input('entered num of sec '))

if t_sec >= 60:
    t_year = t_sec // 31104000
    t_month = t_sec // 2592000  # взял количество дней как 30
    t_day = t_sec // 86400
    t_hour = t_sec // 3600
    t_min = t_sec // 60
    t_sec = t_sec % 60

    if t_month >= 12:
        t_month = t_month % 12
    if t_day >= 30:
        t_day = t_day % 30
    if t_hour >= 24:
        t_hour = t_hour % 24
    if t_min > 60:
        t_min = t_min % 60
    print('Time:', '\n',
          'Years ', t_year, '\n',
          'Months ', t_month, '\n',
          'Days ', t_day, '\n',
          'Hours ', t_hour, '\n',
          'Minutes ', t_min, '\n',
          'Seconds ', t_sec, sep='')
else:

    print('Time: ', 00, ':', 00, ':', 00, ':', 00, ':', 00, ':', t_sec, sep='')
