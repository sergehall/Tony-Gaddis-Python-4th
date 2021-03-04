# math quiz

import random

a = random.randint(-1000, 1000)
b = random.randint(-1000, 1000)
c = a + b
print('{:>6}'.format(a))
print('+', '{:>4}'.format(b))
user_answer = int(input("Please enter the total of these two numbers:\n"))
if user_answer == c:
    print("Congratulations! Your answer", c, "is correct.")
else:
    print('Your answer is wrong, the correct answer: ', c)

