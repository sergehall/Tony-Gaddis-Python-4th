# Turtle graphics
import turtle

num = int(input("How many squares? : "))
size_start = int(input("The size of the side of the square? : "))
turtle.pensize(3)
turtle.speed(10)
for i in range(num):
    turtle.forward(size_start)
    turtle.left(90)
    turtle.pencolor('red')
    turtle.forward(size_start)
    turtle.left(90)
    turtle.pencolor('blue')
    turtle.forward(size_start)
    turtle.pencolor('green')
    turtle.left(90)
    turtle.forward(size_start)
    turtle.left(90)
    size_start += 20

turtle.textinput('Exit', 'Enter any character')
