# The game simulates multiple games with a single deck. When the cards
# run out, the game ends. The game is played by computer against computer.

# 9. Имитация игры в блек-джек. Ранее в этой главе вы рассмотрели программу
# card_dealer.py, которая имитирует раздачу игральных карт из колоды на руки.
# Усовершенствуйте программу так, чтобы она имитировала упрощенную версию
# игры в блекджек между двумя виртуальными игроками. Карты имеют приведенные
# ниже значения.
# • Числовым картам присвоено значение, которое на них напечатано.
# Например, значе- ние двойки пик равняется 2, значение пятерки бубей
# равняется 5.
# • Валетам, дамам и королям присвоено значение 1 О.
# • Тузам присвоено значение 1 или 11 в зависимости от выбора игрока.
# Программа должна раздавать карты каждому игроку до тех пор, пока карты на
# руках у одного из игроков не превысят 21 очко. Когда это происходит,
# другой игрок становится победителем. (Может возникнуть ситуация,
# когда карты на руках у обоих игроков превысят 21 очко; в этом случае
# победителя нет.) Программа должна повторяться до тех
# пор, пока все карты не будут розданы. Если игроку сдан туз, то программа
# должна определить значение этой карты согласно следующему правилу: туз
# равняется 11 очкам, если в результате добавления этой карты
# стоимость комбинации

import random


# Эта программа применяет словарь в качестве колоды карт.
def main():
    # Создать колоду карт.
    deck = create_deck()

    count_win(deck)


#  функция подсчитывает количество ничей, побед 1 и 2 игрока.
def count_win(deck):
    no_one = 0
    wins_1 = 0
    wins_2 = 0
    num_of_game = 0
    # Раздать карты.
    while len(deck) > 0:
        nobody_won, count_1_won, count_2_won = deal_cards(deck)
        no_one += nobody_won
        wins_1 += count_1_won
        wins_2 += count_2_won
        num_of_game = (no_one + wins_1 + wins_2)

    print("***************************")
    print('Total games played = ', num_of_game)
    print('The first player won = ', wins_1)
    print('The second player won = ', wins_2)
    print('No one won = ', no_one)


# Функция create_deck возвращает словарь, представляющий колоду карт.
def create_deck():
    # Создать словарь, в котором каждая карта и ее значение хранятся в виде
    # пар ключ/значение. Пустые строки 113, 119 и 125 вставлены, чтобы было
    # легче читать программный код.
    deck = {'Ace of Spades': 11, '2 of Spades': 2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
            '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
            '10 of Spades': 10, 'Jack of Spades': 10,
            'Queen of Spades': 10, 'King of Spades': 10,

            'Ace of Hearts': 11, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 11, '2 of Clubs': 2, '3 of Clubs': 3,
            '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
            '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
            '10 of Clubs': 10, 'Jack of Clubs': 10,
            'Queen of Clubs': 10, 'King of Clubs': 10,

            'Ace of Diamonds': 11, '2 of Diamonds': 2, '3 of Diamonds': 3,
            '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
            '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
            '10 of Diamonds': 10, 'Jack of Diamonds': 10,
            'Queen of Diamonds': 10, 'King of Diamonds': 10}

    return deck


# Функция deal cards разыгрывает одну руку до победы одного или ничьей
# и возращает 1 у токго кто победил или ничья что бы в дальнейшем можно было
# сложить эти победы.
def deal_cards(deck):
    blackjack = 21
    print("Card distribution number #", len(deck), sep="")
    player1_hand = {}
    player2_hand = {}

    no_one_won = 0
    count_1_won = 0
    count_2_won = 0

    # Инициализировать накопитель для количества карт на руках.
    hand_value1 = 0
    hand_value2 = 0

    # Раздать карты и накопить их значения.
    while hand_value1 <= blackjack or hand_value2 <= blackjack:

        player1_hand = {}
        player2_hand = {}

        try:
            # card, value = deck.popitem() # вариант из книги снимает
            # с конца словаря это с питон3.7 Случайный ключ и значение
            card1, value1 = random.choice(list(deck.items()))
            # print(hand_value1, '+', value1, '=', hand_value1 + value1)
            if (hand_value1 + value1) > blackjack:
                player1_hand.update({card1: value1})
                if card1 == 'Ace of Diamonds' \
                        or card1 == 'Ace of Spades' \
                        or card1 == 'Ace of Hearts' \
                        or card1 == 'Ace of Clubs':
                    value1 = 1
                    player1_hand.update({card1: value1})

            else:
                player1_hand.update({card1: value1})

            del deck[card1]

            card2, value2 = random.choice(list(deck.items()))
            if (hand_value2 + value2) > blackjack:
                player2_hand.update({card2: value2})
                if card2 == 'Ace of Diamonds' \
                        or card2 == 'Ace of Spades' \
                        or card2 == 'Ace of Hearts' \
                        or card2 == 'Ace of Clubs':
                    value2 = 1
                    player2_hand.update({card2: value2})
            else:
                player2_hand.update({card2: value2})

            del deck[card2]

            if hand_value1 >= blackjack:
                break
            if hand_value2 >= blackjack:
                break

        except IndexError:
            break
        print("First Player's Card - ", end="")
        print(player1_hand)
        print("Second Player's Card - ", end="")
        print(player2_hand)
        hand_value1 += value1
        hand_value2 += value2

    print()
    # Показать величину карт на руках.
    print("The first player's hand :", hand_value1, sep="")
    print("The second player's hand :", hand_value2, sep="")

    if hand_value1 == blackjack and hand_value1 != blackjack:
        count_1_won = 1
        print('The winner is Player 1')

    if hand_value2 == blackjack and hand_value2 != blackjack:
        count_2_won = 1
        print('The winner is Player 2')

    if hand_value1 == hand_value2 or (
            hand_value1 > blackjack and hand_value2 > blackjack):
        no_one_won = 1
        print('No one won.')

    if hand_value1 <= blackjack < hand_value2:
        count_1_won = 1
        print('The winner is Player 1')

    if hand_value2 <= blackjack < hand_value1:
        count_2_won = 1
        print('The winner is Player 2')

    if blackjack >= hand_value1 and blackjack >= hand_value2:
        if hand_value1 > hand_value2:
            count_1_won = 1
            print('1 player won.1')
        if hand_value2 > hand_value1:
            count_2_won = 1
            print('2 player won.2')

    print()
    return no_one_won, count_1_won, count_2_won


main()
