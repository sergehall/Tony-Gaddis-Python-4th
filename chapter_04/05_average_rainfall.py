# # average rainfall

years = int(input("How many years of data you want to enter?: "))
months = 0
total_rainfall = 0
average_rainfall = 0
# there will be a nested loop. One for year one for months within year loop.
for i in range(years):
    print()
    for j in range(12):
        print("Please enter year", years, "month", j + 1,
              "rainfall amount in inches", end='')
        rainfall = float(input(": "))
        total_rainfall = round(total_rainfall + rainfall, 2)
        months += 1
    average_rainfall = round(total_rainfall / months, 2)
print()
print('Years = ', years, '\n', 'Months = ', months, '\n', 'Total_rainfall = ',
      total_rainfall, '\n',
      'Average_rainfall = ', average_rainfall, sep='')