# calories burned

cal_per_min = 4.2

print("Minutes\t\tCalories")

for mins in range(10, 31, 5):
    calories = mins * cal_per_min
    print(mins, "\t\t", calories)
