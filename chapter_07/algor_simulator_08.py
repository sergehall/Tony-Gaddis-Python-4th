# 8. Напишите инструкцию, которая создает двумерный список с 5 строками
# и 3 столбцами. Затем напишите вложенные циклы, которые получают от
# пользователя целочисленное значение для каждого элемента в списке.

COLM = int(input('Columns: '))
ROWS = int(input('Rows: '))

two_dimensional_list = [[int(input('Num: ')) for i in range(COLM)]
                        for j in range(ROWS)]
print(two_dimensional_list)
