# random number guessing game
import random


def main():
    # it should ask user again and again until user guesses it.
    keep_going = 1
    ran_num = random_number_generator()
    user_number = int(
        input("Please try to guess random number from 1 through 100: "))
    count_guess = 1

    while keep_going == 1:
        if not compare_numbers(ran_num, user_number):
            keep_going = 1
            user_number = int(input("Please try again: "))
            count_guess += 1
        else:
            keep_going = 0
    print("You have found correct number after", count_guess, "tryings.")


def random_number_generator():
    ran_num = random.randint(1, 100)
    return ran_num


def compare_numbers(ran_num, user_number):
    if ran_num > user_number:
        print("Too low, try again.")
        status = False
    elif ran_num < user_number:
        print("Too high, try again.")
        status = False
    else:
        print()
        print("Congratulations!. You found the number", ran_num)
        status = True
    return status


main()
