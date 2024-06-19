import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
total_guesses = len(data)
guessed_state = []


while len(guessed_state) < total_guesses:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{total_guesses} Guessed",
                                    prompt="What is another state's name??").title()
    # title case makes the words with first letter capital
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append()
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

        # t.write(state_data.state.item())
        # The above statement only extracts the name of state without involving other info


screen.exitonclick()
