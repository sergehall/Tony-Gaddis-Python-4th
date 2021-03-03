# February Days

year = int(input('Enter a year: '))

if (year % 400) == 0:
    print(' In February', year, 'has 29 days.')
elif (year % 100) != 0 and (year % 4) == 0:
    print('In February', year, 'has 29 days.')
else:
    print('In February', year, 'has 28 days.')
