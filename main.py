import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle_screen = turtle.Turtle()
turtle_screen.shape(image)
screen.tracer(0)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_state = []

while len(guess_state) < 50:
    user_answer = screen.textinput(title=f"{len(guess_state)}/50 States", prompt="Enter state").title()
    if user_answer == "Exit":
        break
    if user_answer in all_states:
        screen.update()
        location = data[data.state == user_answer]
        state_loc = turtle.Turtle()
        state_loc.hideturtle()
        state_loc.penup()
        state_loc.goto(int(location.x), int(location.y))
        state_loc.write(arg=user_answer, font=("Ariel", 8, "normal"))
        guess_state.append(user_answer)




