import sys
import time
from turtle import Screen
from paddle import Paddle
from pong_ball import Ball
from score_board import ScoreBoard

# TODO: 1. Create the screen
# TODO: 2. Create and move a paddle
# TODO: 3. Create another paddle
# TODO: 4. Create the ball and make it move
# TODO: 5. Detect collision with wall and bounce
# TODO: 6. Detect collision with paddle
# TODO: 7. Detect when paddle misses
# TODO: 8. Keep score

PADDLE_POSITIONS = ((350, 0), (-350, 0))

screen = Screen()
# background color of the TurtleScreen.
screen.bgcolor("#724F41")
# Set title of turtle-window
screen.title("My Pong Game")
# Set the size and position of the main window.
screen.setup(width=800, height=600)

# Turns turtle animation on/off and set delay for update drawings.
screen.tracer(0)


def update_scr(sleep_time=0.07):
    """update turtle screen"""
    # Perform a TurtleScreen update.
    screen.update()
    # Delay execution for a given number of seconds or sub-second
    time.sleep(sleep_time)


def play():
    """

    :return:
    """
    board.game_is_on = True
    while board.game_is_on:
        update_scr(sleep_time=a_ball.move_speed)

        # detect collision with top/bottom walls
        if a_ball.hit_wall():
            a_ball.bounce_y()
        # detect collision with paddles
        if a_ball.hit_paddle(paddles=(r_paddle, l_paddle)):
            a_ball.bounce_x()
        else:
            # detect when paddle misses the ball
            miss_status = a_ball.paddle_misses()
            if miss_status > -1:
                # keeping score - increase match winner score
                board.add_a_point(miss_status)
                # reset ball pos and direction after an ended match
                a_ball.ball_reset()
                # a short delay after an ended match
                time.sleep(1.4)

        # moving the pong ball
        a_ball.move()


board = ScoreBoard()  # scoreboard
r_paddle = Paddle(start_pos=PADDLE_POSITIONS[0])  # right paddle
l_paddle = Paddle(start_pos=PADDLE_POSITIONS[1])  # left paddle
a_ball = Ball()  # pong ball

# Set focus on TurtleScreen (in order to collect key-events)
screen.listen()

# Bind fun to key-press event of key if key is given,
# or to any key-press-event
# controlling left paddle
# quit the game with key q
screen.onkeypress(key="q", fun=board.quit)
screen.onkeypress(key="Up", fun=r_paddle.up)
screen.onkeypress(key="Down", fun=r_paddle.down)
# controlling left paddle
screen.onkeypress(key="w", fun=l_paddle.up)
screen.onkeypress(key="s", fun=l_paddle.down)

# game logic loop
play()

# Shut the turtlegraphics window.
screen.bye()

# Go into mainloop until the mouse is clicked.
# Bind bye() method to mouseclick on TurtleScreen.
# screen.exitonclick()
