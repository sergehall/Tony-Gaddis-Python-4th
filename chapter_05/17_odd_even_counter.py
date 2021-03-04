# odd/even counter
# Счетчик четных/нечетных чисел.
import random


def even_odd():
    even = 0
    odd = 0
    for i in range(1, 101):
        num = random.randint(1, 501)
        print(num)
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


print("There are", even_odd()[0], "even numbers and", even_odd()[1],
      "odd numbers in the list.")
