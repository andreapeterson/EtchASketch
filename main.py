import turtle as t


turtle = t.Turtle()
screen = t.Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def move_right():
    turtle.right(5)


def move_left():
    turtle.left(5)


def clear_screen():
    turtle.clear()
    turtle.setposition(0,0)
    turtle.clear()


screen.listen()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()
