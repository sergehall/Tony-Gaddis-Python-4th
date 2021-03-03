
# Ingredient Adjuster

# Ask user how many cookies he or she wants
cookie=int(input("Enter the amount of cookies you want: "))
sugar = 1.5
oil = 1
pounder = 2.75
print(sugar * cookie, ' сахара.\n',
      oil * cookie, ' масла.\n',
      pounder * cookie, ' муки.', sep="")
