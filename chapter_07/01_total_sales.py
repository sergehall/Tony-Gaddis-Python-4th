# 1. Общий объем продаж. Разработайте программу, которая просит пользователя
# ввести продажи магазина за каждый день недели. Суммы должны быть сохранены
# в списке. Примените цикл, чтобы вычислить общий объем продаж за неделю и
# показать результат.

def main():
    days_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    daily_sales_week = []
    total = 0
    for daily_sales in days_week:
        print(daily_sales, ': ', end='')
        daily_sales = int(input())
        daily_sales_week.append(daily_sales)
    for i in daily_sales_week:
        total += i

    print('daily_sales_week', daily_sales_week)
    print('Sales per week = ', total)


main()