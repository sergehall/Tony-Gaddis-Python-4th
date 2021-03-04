# sum of numbers

print("-------------------------------------------------------------")
print("Enter a positive number to continue or negative number to end")
print("-------------------------------------------------------------")
# ask user to enter a series of positive numbers
num = int(input("Enter number: "))
i = 0
while num >= 0:
    i += num
    num = int(input("Enter number: "))
print()
print("The total of your number entered is ", i, ".", sep="")
