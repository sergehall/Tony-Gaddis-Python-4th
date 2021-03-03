# age classifier Классификатор возраста.

age = int(input("Please enter your age: "))

if 1 >= age > 0:
    print("Infant!")
elif 1 < age < 13:
    print("Child!")
elif 13 <= age < 20:
    print("Teenager!")
elif age >= 20:
    print("Adult!")
else:
    print("The age you entered is not valid.")
