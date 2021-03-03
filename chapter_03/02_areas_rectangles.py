# areas of rectangles.

rec1_len = int(input("Enter the length of rec 1: "))
rec1_wid = int(input("Enter the width of rec 1: "))

rec2_len = int(input("Enter the length of rec 2: "))
rec2_wid = int(input("Enter the width of rec 2: "))
area1 = rec1_len * rec1_wid
area2 = rec2_len * rec2_wid

# compare the areas
if area1 > area2:
    print("Area of rectangle 1:", area1,
          "is greater than the area of rectangle 2:", area2)
elif area1 < area2:
    print("Area of rectangle 2:", area2,
          "is greater than the area of rectangle 1:", area1)
else:
    print("The areas of two rectangle is same! And it is", area1)
