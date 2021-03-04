# tuition increase

tuition = 8000
increase_rate = 0.03

# print headings
print("Years\tTuition")

for y in range(1, 6, 1):
    tuition_inc = tuition * increase_rate
    tuition += tuition_inc
    print(y, "\t\t$", format(tuition, ",.2f"), sep='')
