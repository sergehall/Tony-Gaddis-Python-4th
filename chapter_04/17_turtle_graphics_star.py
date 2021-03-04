# 17. Черепашья графика: звездочный узор.
import turtle

SIZE = 300
FACES = 10
turtle.speed(10)
turtle.pensize(5)
turtle.pencolor('red')
for i in range(FACES):
    turtle.forward(SIZE)
    turtle.left(135)

turtle.textinput('Exit', 'Enter any character for Exit')