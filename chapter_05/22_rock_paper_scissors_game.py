# rock, paper, scissors game
import random


def main():
    more = "y"
    while more == "y":
        first_players = int(input('Entered: '
                                  '1 if rock, '
                                  '2 if scissors, '
                                  '3 if paper\n'))
        comp_players = random.randint(1, 3)
        scissors_rock_paper(first_players, comp_players)
        print("If you want to play again enter 'y' , 'no' any ch.")
        more = input()


def scissors_rock_paper(player, comp):
    if player == comp:
        print('Draw, try again', 'comp_players', '=', comp, '\n')
        # player = int(input('Entered: 1 if rock, '
        #                           '2 if scissors, '
        #                           '3 if paper.\n'))
        # comp_players = random.randint(1, 3)
        # scissors_rock_paper(first_players, comp_players)
    elif player == 1 and comp == 2:
        print('You Win!', 'computer', '=', comp)
    elif player == 2 and comp == 3:
        print('You Win!', 'computer', '=', comp)
    elif player == 3 and comp == 1:
        print('You Win!', 'computer', '=', comp)
    elif player == 1 and comp == 3:
        print('You Lost!', 'computer', '=', comp)
    elif player == 2 and comp == 1:
        print('You Lost!', 'computer', '=', comp)
    elif player == 3 and comp == 2:
        print('You Lost!', 'computer', '=', comp)


main()
