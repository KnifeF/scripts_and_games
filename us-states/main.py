from turtle import Screen
from states import *

# TODO: 1. Create the screen using states img as bg
# TODO: 2. Create an input window to guess a state name
# TODO: 3. Check when the user's input is correct (check against 50 states extracted from csv file)
# TODO: 4. For correct a answer, Place the state name on the map at it's x,y position, using turtle library
# TODO: 5. Keep track on Num of correct answers - Num/50 States
# TODO: 6. End game when the user answered all the states in the map correctly

# Set up the screen
screen = Screen()
# Set title for window
screen.title("Name the States")
# Set background image
screen.bgpic(picname="blank_states_img.gif")
# Set the size and position of the main window.
screen.setup(width=725, height=491)

my_states = States()

game_is_on = True
while game_is_on:
    # Create an input window to guess a state name
    # input for user to enter a state name - Pop up a dialog window for input of a string
    # Keep track on Num of correct answers
    user_guess = screen.textinput(title=f"{my_states.correct_answers}/{N_STATES} States Correct",
                                  prompt="What's another state name?")
    if user_guess:
        # Check when the user want to exit game, and save the states that he hasn't guessed yet to a csv file
        # Check when the user's input is correct. For a correct answer,
        # Place the state name on the map at it's x,y position, using turtle library
        if user_guess.lower() == "exit" or user_guess.lower() == "quit":
            my_states.save_missed_states()
            game_is_on = False
        elif my_states.is_correct_state(user_guess):
            # End game when the user answered all the states in the map correctly
            if my_states.has_all_states():
                game_is_on = False

# Go into mainloop until the mouse is clicked.
screen.exitonclick()
