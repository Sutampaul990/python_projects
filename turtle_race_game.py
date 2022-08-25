
from turtle import Turtle,Screen
import random


is_race_on=False
screen=Screen()
screen.setup(height=400,width=500)
user_bet = screen.textinput(title="Make your bet : ",prompt="Which turtle will win the race : ")
turtle_color=["red","green","yellow","blue","orange","purple"]
y_length=[100,60,20,-20,-60,-100]
all_turtles=[]


for i in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_color[i])
    new_turtle.goto(x=-230,y=y_length[i])
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    for i in all_turtles:
        if i.xcor() > 230:
            is_race_on=False
            winning_color=i.pencolor()
            if(winning_color==user_bet):
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            
        rand_distance=random.randint(0,10)
        i.forward(rand_distance)
    





screen.exitonclick()