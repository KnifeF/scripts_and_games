import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

'''
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. 
On the next level, the car speed increases.
4. When the turtle collides with a car, it's game over and everything stops.
'''
# TODO: 1. Create the screen- V
# TODO: 2. Create and move the Player- V
# TODO: 3. Create random cars and make them move- V
# TODO: 4. Detect collision with the finish line- V
# TODO: 5. Detect collision with a car- V
# TODO: 6. End game when the turtle is hit by a car- V
# TODO: 7. Manage scoreboard/levels and change difficulty for each level- V


CAR_DELAY = 6

# Create the screen
screen = Screen()
# Set the size and position of the main window.
screen.setup(width=600, height=600)
# Turns turtle animation on/off and set delay for update drawings.
screen.tracer(0)

# Create a turtle player that starts at the bottom of the screen
leonardo = Player()
# Set focus on TurtleScreen
screen.listen()
# listen for the "Up" keypress to move the turtle north.
screen.onkeypress(key="Up", fun=leonardo.walk)

# create an obj that manages cars
manage_cars = CarManager()

# create a Scoreboard obj, that keeps track of which level the user is on.
# Every time the turtle player does a successful crossing, the level should increase.
# When the turtle hits a car, GAME OVER should be displayed in the centre.
manage_levels = Scoreboard()
# displays current level
manage_levels.display_level()

game_is_on = True
c = 0
while game_is_on:
    time.sleep(0.1)  # a short delay
    screen.update()  # Perform a TurtleScreen update.

    # every 6 loop iterations create a new car to the cars list
    if c % 6 == 0:
        # Append a new Car obj to the end of the list.
        # manage_cars.cars.append(Car())
        manage_cars.create_car()

    # checks if a car hit the turtle when it crossed the road
    if leonardo.hit_car(cars=manage_cars.cars):
        # displays Game Over to the screen when a car crash with the turtle occurred
        manage_levels.game_ended()
        game_is_on = False
    # When the turtle hits the top edge of the screen, it
    # moves back to the original position and the player levels up.
    # On the next level, the car speed increases.
    elif leonardo.reach_finishline():
        leonardo.reset_position()
        manage_levels.next_level()
        manage_levels.display_level()
        manage_cars.increase_speed()

    # moves the cars forward
    manage_cars.move_cars()
    c += 1

# Go into mainloop until the mouse is clicked.
screen.exitonclick()
