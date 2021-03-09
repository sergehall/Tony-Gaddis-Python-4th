# # 7. Победители Мировой серии. Среди исходного кода главы 9, а также в
# подпапке data "Решений задач по программированию" соответствующей главы вы
# найдете файл WorldSeriesWiпners.txt. Этот файл содержит хронологический
# список командпобедителей Мировой серии по бейсболу с 1903 по 2019 годы. (
# Первая строка в файле является названием команды, которая победила в 1903
# году, последняя строка - названием команды, которая победила в 2019 году.
# Обратите внимание, что Мировая серия не проводилась в 1904 и 1994 годах. В
# файле имеются указывающие на это пометки.) Напишите программу, которая
# читает этот файл и создает словарь, в котором ключи это названия команд,
# а связанные с ними значения - количество побед команды в Мировой серии.
# Программа должна также создать словарь, в котором ключи - это годы,
# а связанные Программа должна предложить пользователю ввести год в диапазоне
# между 1903 2009 годами и должна вывести название команды, которая выиграла
# Мировую серию в том году и количество побед команды в Мировой серии.

from collections import Counter


def main():
    # создаем список все команд победивших и делаем его глобальный что бы
    # передовать в функции и делать из него словари по заданию.
    winners_list = []

    def creat_list():
        new_file = open('WorldSeriesWinners.txt', 'r')
        content = new_file.readline()
        year = 1903

        while content != '':
            if year == 1904 or year == 1994:
                #  добовляем в список когда не было серии запись
                #  о том что не было серии
                content = content.rstrip()
                winners_list.append('World Series Not Played')
                winners_list.append(content)
                year += 2
                content = new_file.readline()

            else:
                content = content.rstrip()
                winners_list.append(content)
                year += 1
                content = new_file.readline()

        new_file.close()

    creat_list()

    def dict_count_win(list_winner):
        dict_count_win = dict(
            Counter(list_winner))  # создает словарь ключ название команды,
        # значение сколько раз встречается в списке
        # dict_count_win_sort = Counter(list_winner)  # Сортирует от
        # большего к меньшему по значению
        # print(dict_count_win)  # вспомогательный что бы понимать что я получаю
        # print(dict_count_win_sort)  # вспомогательный что бы
        # понимать что я получаю

        return dict_count_win

    def dict_year_team(list_winner):
        year_team_dict = {}
        year = 1903

        for i in list_winner:
            year_team_dict.update({year: i})
            year += 1

        return year_team_dict

    def search_result():
        # в начале год ноль, когда введе правильно у него будет значение
        # правильного года попадающий в диапазон запрашиваемых лет.
        search_year = 0
        year = False
        while year == False:
            try:
                search_year = int(
                    input('Enter year in the range 1903 - 2019: '))
                if search_year < 1903 or search_year > 2019:
                    print('Enter the correct year, between 1903 and 2019!')
                    search_year = int(input('Enter year: '))
                else:
                    year = True

            except ValueError:
                print('Enter numbers not string, between 1903 and 2019!')

        name_team = dict_year_team(winners_list).get(search_year)
        # по году вохзращает название победившей команды. dict_year_team(
        # winners_list) словарь в нем ключ - название команды, значение -
        # количество побед.

        count_won_team = dict_count_win(winners_list).get(name_team)
        # берет название команды выше и проверяет в словаре где ключ -
        # название, значение - количество побед и берет оттуда количество
        # побед. dict_count_win(winners_list) тут словарь все команды ключ год,
        # значение название команды

        print()
        print('The winner World Series ' + str(search_year) + ' is',
              str(name_team) + '.')
        if search_year == 1904 or search_year == 1994:
            pass
        else:
            print('And it has won the cup ', count_won_team, 'times.')

    search_result()


main()
