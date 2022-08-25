import turtle as t
from turtle import Turtle,Screen
import random


tinny_turtle = Turtle()
# tinny_turtle.shape("turtle")
t.colormode(255)
 

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    color=(r, g, b)
    return color

tinny_turtle.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tinny_turtle.color(random_color())
        tinny_turtle.circle(100)
        tinny_turtle.setheading(tinny_turtle.heading() + size_of_gap)

draw_spirograph(5)








screen = Screen()
screen.exitonclick()