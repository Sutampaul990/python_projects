from turtle import Turtle,Screen, pendown, penup

tin=Turtle()
screen=Screen()

def move_forward():
    tin.forward(10)
def move_backward():
    tin.back(10)
def move_right():
    tin.right(10)
def move_left():
    tin.left(10)
def clear():
    tin.clear()
    tin.penup()
    tin.home()
    tin.pendown()

    
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="c",fun=clear)

screen.exitonclick()