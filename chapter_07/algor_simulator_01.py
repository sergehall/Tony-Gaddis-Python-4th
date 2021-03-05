# 1. Напишите инструкцию, которая создает список с приведенными далее
# строковыми значениями: 'Эйнштейн', 'Ньютон', 'Коперник' и 'Кеплер'.

list_star = []
num_star = int(input('Num star '))
for i in range(num_star):
    print('star ', i + 1, ': ', sep='')
    star_name = input()
    list_star.append(star_name)
print(list_star)
