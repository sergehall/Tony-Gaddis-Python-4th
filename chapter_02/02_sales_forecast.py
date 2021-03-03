plan_sum = float(input("Введите планируемую сумму продаж ? "))
profit = ((plan_sum / 100) * 0.23) * 100
print('Вы заработаете $', format(profit, ',.2f'), sep='')
