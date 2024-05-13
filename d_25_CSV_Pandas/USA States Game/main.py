import pandas
import turtle
from populate_state import StateObject

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv('50_states.csv')
all_states = states.state.to_list()

answered_states = []

while len(answered_states) < 51:
    answer = screen.textinput(title=f"{len(answered_states)}/50 Guessed states", prompt="Enter state name?").capitalize()
    if answer == 'Exit':
        missed_states = [state for state in all_states if state not in answered_states]

        data_dict = {
            'state': missed_states,
        }

        df = pandas.DataFrame(data_dict)
        df.to_csv('states_to_learn.csv')

        break

    if answer in all_states and answer not in answered_states:
        answered_states.append(answer)
        state_data = states[states.state == answer]
        state = StateObject(x=int(state_data.x), y=int(state_data.y), text=state_data.state.item())


