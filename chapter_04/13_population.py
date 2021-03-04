# population

# ask user to enter inputs
population = int(input("Enter the population of organisms: "))
up_everyday = float(input("Enter the daily increase as percentage "
                          "(for example 30 for %30): "))
days = int(input("Enter the days to multiply: "))
total = 0
for i in range(1, days + 1):
    if i == 1:
        print('Day', i, population)
    else:
        increment = population * (up_everyday/100)
        population = increment + population
        print('Day', i, round(population, 3))