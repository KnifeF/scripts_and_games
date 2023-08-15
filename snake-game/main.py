import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# TODO: 1. Create a snake body
# TODO: 2. Move the snake
# TODO: 3. Control the snake
# TODO: 4. Detect collision with food
# TODO: 5. Create a scoreboard
# TODO: 6. Detect collision with wall
# TODO: 7. Detect collision with tail


screen = Screen()
# Set the size and position of the main window.
screen.setup(width=600, height=600)
# background color of the TurtleScreen.
screen.bgcolor("black")
# Set title of turtle-window
screen.title("My Snake Game")
# Turns turtle animation on/off and set delay for update drawings.
screen.tracer(0)

# creates Food, Snake, Scoreboard objs
tasty_food = Food()
my_snake = Snake()
score = Scoreboard()

# Set focus on TurtleScreen (in order to collect key-events)
screen.listen()
# Bind fun to key-press event of key if key is given,
# or to any key-press-event
screen.onkeypress(key="Up", fun=my_snake.up)
screen.onkeypress(key="Down", fun=my_snake.down)
screen.onkeypress(key="Right", fun=my_snake.right)
screen.onkeypress(key="Left", fun=my_snake.left)

game_is_on = True
while game_is_on:
    # Perform a TurtleScreen update.
    screen.update()
    # Delay execution for a given number of seconds or sub-second
    time.sleep(0.1)
    # moving the snake
    my_snake.move()
    # detect collision with food
    if my_snake.head.distance(tasty_food) < 15:
        # increases total game score
        score.increase_score(score_val=tasty_food.score_val)
        # increases snake's length
        my_snake.increase_len()
        # generate food on randomized pos on scr
        tasty_food.rand_pos()
    # detect collision with a wall
    if my_snake.detect_hit_wall():
        # Displays updated score on screen.
        score.game_over(wall=True)
        game_is_on = False
        print("you hit wall!")
    if my_snake.eat_itself():
        # Displays updated score on screen.
        score.game_over(tail=True)
        game_is_on = False
        print("the snake has eaten it's tail!")

# Go into mainloop until the mouse is clicked.
# Bind bye() method to mouseclick on TurtleScreen.
screen.exitonclick()
