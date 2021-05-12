from turtle import *
import turtle
import pandas as pd
t=Turtle()
screen=Screen()
screen.title("Indian States Game")
image=r"C:\Users\hp 840g2\Documents\indian_map_game\map2.gif"
screen.addshape(image)
t.shape(image)
state_list=pd.read_csv(r"indian_states.csv")
state_name=state_list["state"].to_list()
guessed_list=[]

score=0

while score<35:
    guess=screen.textinput(str(score)+ "/35 guessed right","Enter State or UT name:").title()
    if guess=="Exit" or guess=="Giveup" or guess=="Give Up":
        for i in state_name:
            if i not in guessed_list:
                guessed_list.append(i)
                coor=state_list[state_list["state"]==i]
                x=coor["x"]
                y=coor["y"]
                t=turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(int(x),int(y))
                t.write(i)
        break

    if guess in state_name:
        if guess not in guessed_list:
            score+=1
            guessed_list.append(guess)
            coor=state_list[state_list["state"]==guess]
            x=coor["x"]
            y=coor["y"]
            t=turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(x),int(y))
            t.write(guess)
if score<35:
    msg=Turtle()
    msg.color("black")
    msg.penup()
    msg.hideturtle()
    msg.goto(-50,300) 
    msg.write("Your score was "+str(score)+" !", align="center",font=("Arial",20,"normal"))

if score==35:
    msg=Turtle()
    msg.color("black")
    msg.penup()
    msg.hideturtle()
    msg.goto(-50,300) 
    msg.write("Congratulation You Won!", align="center",font=("Arial",28,"normal"))

    
screen.exitonclick()
