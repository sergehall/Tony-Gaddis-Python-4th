# pennies for pay
# 7 Мелкая монета для зарплаты. если в рубле 60 копеек)))
# if one ruble is 60 penny
num_day = int(input("Enter the number of days to calculate: "))
dollars = 0
cent = 1
days = 0
total_payroll = 1
total_payroll_dol = 0
total_payroll_cent = 0
if days < 1:
    days += 1
    total_dollars = 0
    total_cents = 1
    print(days, ' Day = ', total_dollars, '.', total_cents, sep='')
while num_day - 1 > 0:
    cent *= 2
    num_day -= 1
    total_dollars = cent // 60
    total_cents = cent % 60
    total_payroll_dol += total_dollars
    total_payroll_cent += total_cents
    days += 1

    print(days, ' Day = ', total_dollars, '.', total_cents, sep='')
print(total_payroll_dol, '.', total_payroll_cent, sep='')

# Мелкая монета для зарплаты. если в рубле 100 копеек
# if one ruble is 100 penny
days_in = int(input("Enter the number of days to calculate: "))
cents = 0.01
total = 0
for i in range(1, days_in + 1):
    if i == 1:
        total += cents
        print('pay day', i, format(cents, ',.2f'))
    else:
        cents *= 2
        total += cents
        print('pay day', i, format(cents, ',.2f'))
print('total', days_in, format(total, ',.2f'))
