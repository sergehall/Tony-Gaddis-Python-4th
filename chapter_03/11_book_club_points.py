# book club points
n_books = int(input("Enter the the number of books purchased: "))

print()
if n_books == 0:
    points = 0
    print("You have been", points, "point awarded with your purchase of",
          n_books, "books.")
elif 2 <= n_books < 4:
    points = 5
    print("You have been", points, "points awarded with your purchase of",
          n_books, "books.")
elif 4 <= n_books < 6:
    points = 15
    print("You have been", points, "points awarded with your purchase of",
          n_books, "books.")
elif 6 <= n_books < 8:
    points = 30
    print("You have been", points, "points awarded with your purchase of",
          n_books, "books.")
elif n_books >= 8:
    points = 60
    print("You have been", points, "points awarded with your purchase of",
          n_books, "books.")
else:
    print("ERROR")
