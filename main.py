from ast import Store
from multiprocessing import set_forkserver_preload
import pandas
import turtle
import numpy

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/Users/jinchoi/Desktop/100days/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv(
    "/Users/jinchoi/Desktop/100days/us-states-game-start/50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    # # Convert the guess to Title case
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [
            state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
