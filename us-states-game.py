import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("US State Game")
image= r"C:\Users\hp 840g2\Documents\python\finding_map\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# answer=screen.textinput(title="Guess The State",prompt="Whats another state name?")
guessed_states=[]
states_loc=pd.read_csv(r"C:\Users\hp 840g2\Documents\python\finding_map\50_states.csv")
states_names=states_loc["state"].to_list()

while len(guessed_states)<50:
    answer=screen.textinput(title=str(len(guessed_states))+"/50 states correct",prompt="Whats another state name?").title()
    if answer=="Exit":
        for i in states_names:
            if i not in guessed_states:
                t=turtle.Turtle()
                t.hideturtle()
                t.penup()
                coordinates=states_loc[states_loc["state"]==i]
                x=coordinates["x"]
                y=coordinates["y"]
                t.goto(int(x),int(y))
                t.write(i)
        break
    
    if answer in states_names:
        guessed_states.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinates=states_loc[states_loc["state"]==answer]
        x=coordinates["x"]
        y=coordinates["y"]
        t.goto(int(x),int(y))
        t.write(answer)
   

screen.exitonclick()