import turtle
import pandas

screen = turtle.Screen()

def create_screen():
    screen.title("U.S States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle_screen = turtle.Turtle()
    turtle_screen.shape(image)
    screen.tracer(0)



def states_game():
    screen.clear()
    create_screen()
    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    data.to_csv("States_to_learn_on_map.csv.csv")
    guess_state = []
    df = pandas.read_csv("States_to_learn_on_map.csv.csv")
    # print(df.state)

    state_loc = turtle.Turtle()
    state_loc.hideturtle()
    state_loc.penup()
    while len(guess_state) < 50:
        user_answer = screen.textinput(title=f"{len(guess_state)}/50 States", prompt="Enter state").title()

        if user_answer in all_states:
            screen.update()
            data_state = data[data.state == user_answer]
            state_loc.goto(int(data_state.x), int(data_state.y))
            state_loc.write(arg=user_answer, font=("Ariel", 8, "normal"))
            guess_state.append(user_answer)
            df = df[df["state"] != user_answer]
            df.to_csv("States_to_learn_on_map.csv")

        elif user_answer == "Exit":
            create_screen()

            stl = df.state

            for state in stl:
                statexy = df[df.state == state]
                state_loc.goto(int(statexy.x), int(statexy.y))
                state_loc.write(arg=statexy.state.item(), font=("Ariel", 8, "normal"))
            screen.update()
            user_answer = screen.textinput(title=f"States Game", prompt="Ready to try again?").title()
            if user_answer == "Yes":
                states_game()
            else:
                screen.exitonclick()
            # states_to_learn = {
            #     "countries to learn": []
            # }
            # for state in all_states:
            #     if state not in guess_state:
            #         states_to_learn["countries to learn"].append(state)
            # data_file = pandas.DataFrame(states_to_learn)
            # data_file.to_csv("States_to_learn.csv")

states_game()
