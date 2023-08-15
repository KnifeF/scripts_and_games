from turtle import Turtle

MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
PADDLE_COLOR = "#BBA14F"


class Paddle(Turtle):
    def __init__(self, start_pos=(350, 0)):
        """Initializes a Paddle obj"""
        super().__init__(shape="square")
        self.create_paddle(start_pos)

    def create_paddle(self, start_pos):
        """
        Creates the paddle body
        """
        self.color(PADDLE_COLOR, "black")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")
        self.penup()
        self.goto(start_pos)

    def up(self):
        """checks current heading of paddles head. move the paddle up"""
        if self.ycor() < 240:
            self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)

    def down(self):
        """checks current heading of paddles head. move the paddle down"""
        if self.ycor() > -240:
            self.goto(x=self.xcor(), y=self.ycor() - MOVE_DISTANCE)
