import random
from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")
tim.color("black", "green")
tim.shape("turtle")

rand_size = random.randint(1, 9)
tim.shapesize(stretch_wid=rand_size, stretch_len=rand_size, outline=rand_size)
screen = Screen()


def move_forwards():
    """
    move turtle forward
    :return:
    """
    tim.forward(10)


def move_backwards():
    """
    move turtle forward
    :return:
    """
    tim.backward(10)


def counter_clockwise():
    """
    move turtle counter-clockwise
    :return:
    """
    tim.left(10)


def clockwise():
    """
    move turtle clockwise
    :return:
    """
    tim.right(10)


def clr_turtle():
    """
    clear drawings in turtle
    :return:
    """
    # Delete the turtle's drawings from the screen. Do not move turtle.
    tim.clear()
    tim.penup()  # Pull the pen up -- no drawing when moving.
    tim.home()  # Move turtle to the origin - coordinates (0,0).
    tim.pendown()  # Pull the pen down -- drawing when moving.


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkeypress(key="c", fun=clr_turtle)


screen.exitonclick()
