# Appraiser of painting works. The paint company found that for every 10 square meters
# meters of wall surface requires 5 liters of paint and 8 hours of work. Company
# charges 2000 rubles per hour for work. Write a program that asks the user to
# enter the surface area of the wall to be painted and the price of a 5-liter paint container.
# The program should show the following data:
# • the number of paint containers required;
# • number of required working hours;
# • cost of paint;
# • cost of work;
# * total cost of painting works.

import math

s_area = float(input('Enter the surface area of the wall to be painted? '))
price_one_cans = int(input('The price one 5L can of paint?  '))
HOURLY_RATE = 2000  # rub/hour


def main():
    how_much_paint_cans(s_area)
    how_many_hours(s_area)
    price_all_paints(s_area, price_one_cans)
    value_work()
    total_cost_work()
    print('Needs cans or can ', how_much_paint_cans(s_area))
    print('Needs hours ', how_many_hours(s_area), ' hours.')
    print('Payments for material ',
          format(price_all_paints(s_area, price_one_cans), ',.2f'), 'rub.')
    print('Payments for time ', format(value_work(), ',.2f'), 'rub.')
    print('Amounts time + material ', format(total_cost_work(), ',.2f'), 'rub.')


def how_much_paint_cans(area):
    one_can = 10  # one can for 10 m**2
    if area % one_can == 0:
        area = area // one_can
        return int(area)
    else:
        area = area // one_can + 1
        return int(area)


def how_many_hours(area):
    s_in_min = 48  # 1 m**2 in 48 min
    time = math.ceil((area * s_in_min) / 60)
    return time


def price_all_paints(area, price):
    price_all = how_much_paint_cans(area) * price
    return price_all


def value_work():
    return how_many_hours(s_area) * HOURLY_RATE


def total_cost_work():
    total = value_work() + price_all_paints(s_area, price_one_cans)
    return total


main()

