# Ingredient Adjuster

# Ask user how many cookies he or she wants
cookie = int(input("Enter the amount of cookies you want: "))
sugar = 1.5
oil = 1
pounder = 2.75
print(sugar * cookie, ' gr. sugar.\n',
      oil * cookie, ' gr. butter.\n',
      pounder * cookie, ' gr. flour.', sep="")
