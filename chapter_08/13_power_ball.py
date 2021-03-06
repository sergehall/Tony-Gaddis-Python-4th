# 13 . Лотерея PowerBall. Для того чтобы сыграть в лотерею PowerBall,
# покупают билет, в котором имеется пять чисел от 1 до 69 и число "PowerBall"
# в диапазоне от 1 до 26. (Эти числа можно выбрать самому либо дать билетному
# автомату их выбрать за вас случайным образом.) Затем в заданный день
# автомат случайным образом отбирает выигрышный ряд чисел. Если первые пять
# чисел совпадают с первыми пятью выигрышными числами в любом порядке,
# и ваше число PowerBall соответствует выигрышному числу PowerBall,
# то вы выигрываете джекпот, который составляет очень крупную сумму денег.
# Если ваши числа совпадают лишь с некоторыми выигрышными числами ,
# то вы выигрываете меньшую сумму в зависимости от того, сколько выигрышных
# номеров совпало . Среди исходного кода главы 8, а также в подпапке data
# "Решений задач по программированию" соответствующей главы вы найдете файл с
# именем pbnumbers.txt, содержащий выигрышные номера PowerBall, которые были
# отобраны между 3 февраля 201 О и 11 мая 2016 (файл содержит 654 наборов
# выигрышных чисел) . Рис. 8.6 показывает пример первых нескольких строк
# содержимого этого файла. Каждая строка в файле содержит набор и последнее
# число в каждой строке является числом PowerBall для этого дня. Например,
# первая строка в файле показывает числа за 3 февраля 201 О, которые
# равнялись 17, 22, 36, 37, 52, и число PowerBall, равное 24.
# Напишите одну или несколько программ, которые работают с этим файлом
# и показывают:
# • 1 О наиболее распространенных чисел , упорядоченных по частоте;
# • 1 О наименее распространенных чисел, упорядоченных по частоте;
# • 10 наиболее "созревших" чисел (чисел, которые не использовались
# долгое время), упорядоченных от наиболее созревших до наименее созревших;
# • частоту каждого числа от 1 до 69 и частоту каждого PowerBall
# числа от 1 до 26.

import collections

open_file = open('pbnumbers.txt', 'r')
content = open_file.readlines()
content_list = []
for i in content:
    i_new = i.rstrip('\n')  # очищаем от '\n'
    content_list.append(i_new)  # add to new list content_list

open_file.close()
print(content_list)
print()

# Создаем три строки: 1) из цифр в каждлй лотереи от 1 до 5;
# 2) список из чисел powerball; 3) все
content_list_5 = ''
content_list_PB = ''
content_list_all = ''
for i in content_list:
    i_new = i[:-3]
    i_PB = i[-2:]
    content_list_5 = content_list_5 + ' ' + i_new
    content_list_PB = content_list_PB + ' ' + i_PB
    content_list_all = content_list_all + ' ' + i

# разбиваем все строки по пробелу что бы в дальнейшем перевести их в int
content_list_5_num = content_list_5.split()
content_list_PB_num = content_list_PB.split()
content_list_all_num = content_list_all.split()

# переводим строки и закидываем в список уже цифрами
content_list_5_num_list = []
content_list_PB_num_list = []
content_list_all_num_list = []

for i in content_list_5_num:
    content_list_5_num_list.append(int(i))

for i in content_list_PB_num:
    content_list_PB_num_list.append(int(i))

for i in content_list_all_num:
    content_list_all_num_list.append(int(i))
print('Создали три списка с числами int внутри; 1) до 5 числа;'
      ' 2) все числа Power Ball; 3) Все.')
print(content_list_5_num_list)
print(content_list_PB_num_list)
print(content_list_all_num_list)
print()

# подсчитываем самые часто встречающиеся цифры получаем вложенный список
# отсортированый по убыванию первое число в подсписке значение и второе
# количество раз встречающееся.
# частоту каждого числа от 1 до 69 и
five = collections.Counter(content_list_5_num_list)
# частота каждого PowerBall числа от 1 до 26.
PB = collections.Counter(content_list_PB_num_list)
# частота всех чисел
all_num = collections.Counter(content_list_all_num_list)
print('Три вложенных списка: 1) частоту каждого числа от 1 до 69 '
      '2) частота каждого PowerBall числа от 1 до 26. '
      '3)  частота всех чисел  ')
print(five.most_common())
print(PB.most_common())
print(all_num.most_common())
print()

high_10 = all_num.most_common()[:10]
low_10 = all_num.most_common()[-10:]
print('1) Из всех 10 самых частых чисел. (19 число самое частое 111 раз '
      'встр-ся). 2) 10 самых редких чисел  ')
print(high_10)  # 10 самых частых чисел 19 число 11 сколько раз
print(low_10)  # 10 самых редких чисел

# частоту каждого числа от 1 до 69 и частоту
# каждого PowerBall числа от 1 до 26.
