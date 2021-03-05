# 3. Статистика дождевых осадков. Разработайте программу, которая позволяет
# пользователю занести в список общее количество дождевых осадков за каждый
# из 12 месяцев. Программа должна вычислить и показать суммарное количество
# дождевых осадков за год, среднее ежемесячное количество дождевых осадков и
# месяцы с самым высоким и самым низким количеством дождевых осадков.

def main():
    def precipitation_month():
        month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                 'Sep', 'Oct', 'Nov', 'Dec']
        prercip_year = []
        total_prercit = 0
        for precip in month:
            print(precip, ': ', end='')
            precip_per_month = int(input())
            prercip_year.append(precip_per_month)
            total_prercit += precip_per_month

        average_precip = total_prercit / len(month)
        max_precip = max(prercip_year)
        min_precip = min(prercip_year)

        min_m_list = []
        for n in range(len(prercip_year)):
            if prercip_year[n] == min_precip:
                min_m_list.append(month[n])

        max_m_list = []
        for n in range(len(prercip_year)):
            if prercip_year[n] == max_precip:
                max_m_list.append(month[n])

        print(prercip_year)
        print('The total rainfall is = ' + str(total_prercit))
        print('The average monthly rainfall is = '
              + str(round(average_precip, 2)))

        print('The minimum rainfall was every '
              + str(min_m_list) +
              ' month = ' + str(min_precip))

        print('The maximum rainfall was every'
              + str(max_m_list) +
              ' month = ' + str(max_precip))

    precipitation_month()


main()