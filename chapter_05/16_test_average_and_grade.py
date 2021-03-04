# test average and grade
# Средний балл и его уровень.

def main():
    my_list_ratings = list_ratings()
    print("----------------------")
    print("Score ", "|", "Letter Grade")
    print("----------------------")
    for i in my_list_ratings:
        print(i, end="")
        print('{:>8}'.format(determine_grade(i)))
    print("Your average is ", calc_average(my_list_ratings), ".", sep="")


def list_ratings():
    ratings_list = []
    n = int(input("How many ratings do you want to enter?:\n"))
    for i in range(n):
        print("Enter the grade for test ", i + 1, ": ", sep="", end="")
        rating = int(input(""))
        ratings_list.append(rating)
    return ratings_list


def calc_average(my_list_ratings):
    total = 0
    for i in my_list_ratings:
        total += i
    average = total // len(my_list_ratings)
    return average


def determine_grade(average):
    if average >= 90:
        return 'A'
    elif 80 <= average <= 89:
        return 'B'
    elif 70 <= average <= 79:
        return 'C'
    elif 60 <= average <= 69:
        return 'D'
    else:
        return 'F'


main()
