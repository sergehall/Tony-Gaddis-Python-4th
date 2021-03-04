# pattern 1
# print the following using loop structures.

# *******
# ******
# *****
# ****
# ***
# **
# *

BASE_SIZE = int(input("Enter number of stars in the main line: "))

for i in range(BASE_SIZE):
    for j in range(BASE_SIZE):
        print('*', end='')
    BASE_SIZE -= 1
    print()
