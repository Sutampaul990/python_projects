import random
import turtle as t
from turtle import Turtle,Screen

tinny_turtle=Turtle()
tinny_turtle.speed("fastest")
tinny_turtle.penup()
tinny_turtle.hideturtle()
# tinny_turtle.shape("turtle")
t.colormode(255)

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
    
#     color=(r, g, b)
#     return color

tinny_turtle.setheading(225)
tinny_turtle.forward(325)
tinny_turtle.setheading(0)

number_of_dots=101

for dot_count in range(1,number_of_dots):
    tinny_turtle.dot(20,random.choice(color_list))
    tinny_turtle.forward(50)
    
    if dot_count % 10 == 0:
        tinny_turtle.setheading(90)
        tinny_turtle.forward(50)
        tinny_turtle.setheading(180)
        tinny_turtle.forward(500)
        tinny_turtle.setheading(0)







screen=Screen()
screen.exitonclick()