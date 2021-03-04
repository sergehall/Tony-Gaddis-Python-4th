# bug collector

bugs_total = 0.0

for day in range(5):
    print("Enter the collected bugs for day", day + 1, end='')
    bugs = int(input(": "))
    # add bugs to accumulator
    bugs_total += bugs
print()
print("The total bugs collected: ", bugs_total)
