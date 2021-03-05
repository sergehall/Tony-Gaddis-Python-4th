# The cost values are randomly assigned and a graph is drawn.
# 14. Круговая диаграмма расходов. Создайте текстовый файл,
# который содержит ваши расходы за прошлый месяц по приведенным ниже статьям:
# • арендная плата;
# • бензин;
# • продукты питания;
# • одежда;
# • платежи по автомашине;
# • прочие.
# Напишите программу Python, которая считывает данные из файла и
# использует пакет matplotlib для построения круговой диаграммы,
# показывающей, как вы тратите свои деньги.

import matplotlib.pyplot as plt
import random


def main():
    # создаем автоматически суммы затрат и вписываем их  в файл spending_
    # per_month.txt.
    list_spending = ['Арендная плата', 'Бензин',
                     'Продукты питания', 'Одежда',
                     'Платежи по ', 'Автомашине', 'Прочие']

    spending_per_month = open('spending_per_month.txt', 'w')

    i = 0
    while i < len(list_spending):
        spending_per_month.write(str(random.randint(100, 10000)) + '\n')
        i += 1
    spending_per_month.close()

    # считываем информацию из файла spending_per_month.txt и
    # создаем на основе данных диограму.
    spen_lst = open('spending_per_month.txt', 'r')
    content = spen_lst.readlines()

    # открываем файл и считываем с него все суммы ,
    # складываем что бы добавить общую сумму в title
    o = open('spending_per_month.txt', 'r')
    con = o.readlines()
    con_list = []
    for i in con:
        i = int(i.rstrip('\n'))
        con_list.append(i)
    o.close()
    con_sum = format(sum(con_list), ',.2f')

    plt.title('Расходы за прошлый месяц = ' + '$ ' + str(con_sum))
    plt.pie(content, labels=list_spending, autopct='%1.2f%%')
    plt.show()


main()
