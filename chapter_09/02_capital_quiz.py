# # 2. Викторина со столицами. Напишите программу, которая создает словарь,
# содержащий в качестве ключей названия американских штатов и в качестве
# значений их столицы. (Список штатов и соответствующих им столиц можно найти
# в Интернете.) Затем программа  должна провести викторину, случайным образом
# выводя название штата и предлагая ввести его столицу. Программа должна
# провести подсчет количества правильных и неправильных ответов. (Как
# вариант, вместо американских штатов программа может использовать названия
# стран и их столиц.)

import random


def main():
    # Function to manually create a dictionary key - state, value - capital.
    # def add_new_pair():
    #     dic_state_capital = {}
    #     cont = 'y'
    #     while cont == 'y':
    #         key_state = input('enter state: ')
    #         value_capital = input('enter capital: ')
    #         new_pair = {key_state: value_capital}
    #         dic_state_capital.update(new_pair)
    #         print('Хотите еще добавить пару штат и столица?')
    #         cont = input('enter y if Yes, any if NO. ')
    #     print(dic_state_capital)
    #
    #
    # add_new_pair()

    # we created a dictionary that would take a long time to manually enter
    dic_state_capital = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
                            'Arizona': 'Phoenix',
                            'Arkansas': 'Little Rock',
                            'California': 'Sacramento', 'Colorado': 'Denver',
                            'Connecticut': 'Hartford', 'Delaware': 'Dover',
                            'Florida': 'Tallahassee',
                            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
                            'Idaho': 'Boise',
                            'Illinios': 'Springfield',
                            'Indiana': 'Indianapolis', 'Iowa': 'Des Monies',
                            'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
                            'Louisiana': 'Baton Rouge',
                            'Maine': 'Augusta', 'Maryland': 'Annapolis',
                            'Massachusetts': 'Boston',
                            'Michigan': 'Lansing', 'Minnesota': 'St. Paul',
                            'Mississippi': 'Jackson',
                            'Missouri': 'Jefferson City', 'Montana': 'Helena',
                            'Nebraska': 'Lincoln',
                            'Neveda': 'Carson City', 'New Hampshire': 'Concord',
                            'New Jersey': 'Trenton',
                            'New Mexico': 'Santa Fe', 'New York': 'Albany',
                            'North Carolina': 'Raleigh',
                            'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
                            'Oklahoma': 'Oklahoma City',
                            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
                            'Rhoda Island': 'Providence',
                            'South Carolina': 'Columbia',
                            'South Dakoda': 'Pierre', 'Tennessee': 'Nashville',
                            'Texas': 'Austin', 'Utah': 'Salt Lake City',
                            'Vermont': 'Montpelier',
                            'Virginia': 'Richmond', 'Washington': 'Olympia',
                            'West Virginia': 'Charleston',
                            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    # запускаем программу
    game(dic_state_capital)


def game(dic_state_capital):
    count_true = 0
    count_false = 0
    game_cont = 'y'
    while game_cont == 'y':
        # random.choice(list(d.keys()))

        country, capital = random.choice(list(dic_state_capital.items()))
        print("What is the capital of", country, end="")
        capital_game = input(': ')
        if capital_game == capital:
            print("Correct!")
            count_true += 1
        else:
            print("Wrong! The correct answer is", capital)
            count_false += 1
        print()
        print('Do you want to play again?')
        game_cont = input("Enter 'y' if Yes, 'any' if No. ")
        print()

    print('Correct answer =', count_true)
    print('Wrong answer =', count_false)


main()

