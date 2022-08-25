import random
import turtle as t
from turtle import Turtle,Screen
tinny_turtle=Turtle()
tinny_turtle.shape("turtle")
t.colormode(255)
# tinny_turtle.color("green")
# tinny_turtle.forward(100)
# tinny_turtle.right(90)
# def square():
#     tinny_turtle.forward(100)
#     tinny_turtle.right(90)
# for i in range(0,4):
    #square()

# def dash_line():
#     tinny_turtle.forward(10)
#     tinny_turtle.pendown()
#     tinny_turtle.forward(10)
#     tinny_turtle.penup()
# for i in range(0,11):
#     dash_line()   

#differnt shapes object
# color=["red","orange","green","yellow","blue","violet","pink","grey","black","CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# angle=360
# def shape():
#     for i in range(3,11):
#         # tinny_turtle.forward(10)
#         tinny_turtle.color(random.choice(color))
#         n=0
#         while n<i:
#             tinny_turtle.right(angle/i)
#             tinny_turtle.forward(10*10)
#             n+=1
#         i+=1
# shape()

#Random Walking Process with Random Colour

directions=[0,90,180,270]



tinny_turtle.pensize(15)
tinny_turtle.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    random_color=(r, g, b)
    return random_color

for i in range(200):
    tinny_turtle.color(random_color())
    tinny_turtle.forward(30)
    tinny_turtle.setheading(random.choice(directions))
    
    







#End of the programme
screen = Screen()#object
screen.exitonclick()