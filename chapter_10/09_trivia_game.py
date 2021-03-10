from random import choice


class Question:

    def __init__(self, question, answer1, answer2, answer3, answer4,
                 num_corr_answer):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__num_corr_answer = num_corr_answer

    def get_question(self):
        return self.__question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_num_corr_answer(self):
        return self.__num_corr_answer

    def set_question(self, question):
        self.__question = question

    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_num_corr_answer(self, num_corr_answer):
        self.__num_corr_answer = num_corr_answer

    def __str__(self):
        return self.__question + "\n" + \
               "1: " + self.__answer1 + "\n" + \
               "2: " + self.__answer2 + "\n" + \
               "3: " + self.__answer3 + "\n" + \
               "4: " + self.__answer4


def main():
    # dic object to dic key name question, value object
    # and list with k for random chose
    print("Two players play, each answering five questions in turn.")
    my_list, my_dic = creat_dict()

    total_1 = 0
    total_2 = 0
    count = len(my_list)
    while count > 0:
        print()
        print("Question #" + str((len(my_dic) + 1) - count))
        chose_question = (chose_random_question(my_list))
        chose_object = my_dic[chose_question]
        print(chose_object)
        if count % 2 == 0:
            answer = int(input("The first player answers: "))
            if answer == chose_object.get_num_corr_answer():
                total_1 += 1
        if count % 2 == 1:
            answer = int(input("The second player answers: "))
            if answer == chose_object.get_num_corr_answer():
                total_2 += 1
        count -= 1

    print()
    print("Correct answers player 1 =", total_1)
    print("Correct answers player 2 =", total_2)
    print()
    if total_1 > total_2:
        print("Congratulations! Player 1 Won!")
    elif total_1 == total_2:
        print("The game is a draw! ")
    else:
        print("Congratulations! Player 2 Won!")


def creat_dict():
    # создали обьекты
    one = Question("What is the first step in the Order of Operations?",
                   "Exponents.",
                   "Addition.",
                   "Brackets.",
                   "Subtraction.",
                   1)

    two = Question("What is notification of superfactorial?",
                   "#.",
                   "!.",
                   "&.",
                   "$.",
                   4)

    three = Question("What does pi equal?",
                     "3.15259.",
                     "6.28318.",
                     "2.7182.",
                     "3.14159.",
                     4)

    four = Question("What is the degree of a triangle?",
                    "90º.",
                    "540º.",
                    "180º.",
                    "270º.",
                    3)

    five = Question("What are the numbers 2, 3, 5, 7, 11 ... ?.",
                    "Primer.",
                    "Odd.",
                    "Composite.",
                    "None of these.",
                    1)

    six = Question("1, 1, 2, 3, 5, 8, 13 ... are called ______ numbers.",
                   "Euler's number.",
                   "Fibonacci.",
                   "Lucky Numbers Slevin.",
                   "Rāmānujan.",
                   2)

    seven = Question("How many parts are there in a triangle?",
                     "9.",
                     "6 times.",
                     "3.",
                     "None of these.",
                     3)

    eight = Question("It is a relation where each element in the domain \n"
                     "is related to one value in the range by some rule.",
                     "Function.",
                     "Solution.",
                     "Graph.",
                     "Equation.",
                     1)

    nine = Question("Who is the Prince of Mathematics?",
                    "Euclid.",
                    "Joseph James Rogan.",
                    "Euler.",
                    "Gauss.",
                    3)

    ten = Question("Which English theoretical physicist authored \n"
                   "The Theory of Everything, and A Brief History of Time?",
                   "Lawrence Krauss.",
                   "Einstein.",
                   "Stephen Hawking.",
                   "Neil deGrasse Tyson.",
                   3)

    # add object to dic key name question, value object
    my_dic_quiz = {"one": one, "two": two, "three": three, "four": four,
                   "five": five, "six": six, "seven": seven, "eight": eight,
                   "nine": nine, "ten": ten}

    # for random chose question
    my_list_question = ["one", "two", "three", "four", "five", "six", "seven",
                        "eight", "nine", "ten"]

    return my_list_question, my_dic_quiz


def chose_random_question(my_list_question):
    # random chose question
    while my_list_question:
        i = choice(my_list_question)
        if i in my_list_question:
            i = choice(my_list_question)
            my_list_question.remove(i)
            return i
        else:
            continue


main()
