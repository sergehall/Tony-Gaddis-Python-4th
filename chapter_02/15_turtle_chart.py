import turtle

turtle.speed(10)
def main():
    turtle.hideturtle()
    square(100, 0, 50, 'red')
    square(-150, -100, 200, 'blue')
    square(-200, 150, 75, 'green')
    square(200, 150, 75, 'green')
    square(-200, 450, 75, 'red')
    square(-450, -550, 445, 'yellow')
    square(500, 500, 305, 'green')
    square(400, -400, 155, 'green')
    turtle.textinput('something', 'Push')


def square(x, y, width, color):
    turtle.penup()  # Поднять перо.
    turtle.goto(x, y)  # Переместить в указанное место.
    turtle.fillcolor(color)  # Задать цвет заливки.
    turtle.pendown()  # Опустить перо.
    turtle.begin_fill()  # Начать заливку.
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()  # Завершить заливку.




main()
