# Male,Female Percentages

male=int(input("Please enter the number of males in the class: "))
female=int(input("Please enter the number of females in the class: "))
total=male+female

p_male=(male/total)*100
p_female=(female/total)*100

print()
print("Male is %", p_male, sep='')
print("Female is %", p_female, sep='')
