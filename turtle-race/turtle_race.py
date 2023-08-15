from turtle import Turtle, Screen
import random

# list of colors to fill turtles
colors_list = ["red", "green", "blue", "yellow", "orange", "purple"]
screen = Screen()
# Set the size and position of the main window.
screen.setup(width=500, height=400)
# Set title of turtle graphics window
screen.title("Turtle Race!")
# Set background image
screen.bgpic("sand_turtle_race.gif")


def bet_popup():
    """
    Pop up a dialog window for input of a string (a turtle color to bet on)
    :return: str - the turtle color in lowercase
    """
    # get a string from the user (value is a string)
    user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a color:")
    return user_bet.lower()


def set_turtles():
    """
    sets start position, shape, speed, colors of the turtles...
    :return:
    """
    # shuffle list to randomize order of colored turtles
    random.shuffle(colors_list)
    racing_turtles = []
    for i in range(len(colors_list)):
        # creates a turtle obj and adds to a list of turtles
        racing_turtles.append(Turtle(shape="turtle", visible=False))
        racing_turtles[i].speed("slowest")  # turtle's speed
        racing_turtles[i].penup()  # Pull the pen up – no drawing when moving.
        racing_turtles[i].color("black", colors_list[i])  # set the pencolor and fillcolor.
        # note: All turtle positions are measured from their center.
        # Move turtle to an absolute position.
        racing_turtles[i].setposition(x=-230, y=50 * (i + 1) - 175)
        racing_turtles[i].showturtle()  # Makes the turtle visible.
    return racing_turtles


def open_turtle_race():
    """
    Creates turtles, and starts moving turtles forward with a changing random paces, until there is a winner
    :return:
    """
    opponent_turtles = set_turtles()  # sets the turtles' properties for the race
    random.shuffle(opponent_turtles)  # shuffle list to randomize order of turtles

    valid_bet = False
    usr_bet = ""
    while not valid_bet:
        usr_bet = bet_popup()
        # checks if the user entered an input of an optional turtle color
        if usr_bet in colors_list:
            valid_bet = True
        else:
            print(f"possible turtles: {colors_list}")  # optional colors to choose

    running_race = True
    # x pos to pass on screen, in order to finish race
    # 230 is 250 - half the width of the turtle.
    edge_x_pos = 215
    while running_race:
        for pretty_turtle in opponent_turtles:
            # Move the turtle forward by the randomized distance.
            pretty_turtle.forward(random.randint(1, 15))
            # turtle position is greater than x pos that represent a cross of the finishing line
            if pretty_turtle.xcor() >= edge_x_pos:
                running_race = False  # ends race (stops while loop)

                # fillcolor of the winner turtle
                winner_color = pretty_turtle.fillcolor()
                winner_out = f"You've won! The {winner_color} turtle is the winner!"
                if usr_bet != winner_color:
                    winner_out = winner_out.replace("won", "lost", 1)

                # Declare winner!
                # prints the winner, and the fillcolor of the winner turtle (also displays on screen)
                print(winner_out)
                # Write text at the current turtle position (displays winner on screen)
                out_turtle = Turtle(visible=False)
                out_turtle.penup()  # Pull the pen up – no drawing when moving.
                out_turtle.write(winner_out, True, align="center")
    return opponent_turtles


# starts a turtle race
my_turtles = open_turtle_race()
# Go into mainloop until the mouse is clicked.
screen.exitonclick()
