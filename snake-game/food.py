from turtle import Turtle
import random


FOOD_COLOR = "#6f3096"


class Food(Turtle):
    def __init__(self):
        """Initializes a Food obj"""
        super().__init__(shape="circle")
        self.penup()  # Pull the pen up – no drawing when moving.
        self.score_val = 20  # food value for score
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # turtle's stretch-factors/outline
        self.color(FOOD_COLOR)  # pencolor
        self.speed("fastest")  # turtle's speed
        self.rand_pos()  # render food on screen

    def rand_pos(self):
        """renders food at a new random location on screen"""
        starting_position = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(starting_position)  # Move turtle to an absolute position.
