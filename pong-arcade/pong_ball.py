from turtle import Turtle

MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
BALL_COLOR = "#BBA14F"


class Ball(Turtle):
    def __init__(self):
        """Initializes a Ball obj"""
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def create_ball(self):
        """
        Creates the ball
        """
        self.color(BALL_COLOR, "black")
        self.shape("square")
        # self.speed("fast")
        self.penup()
        self.goto(0, 0)

    def move(self):
        """
        moves the pong ball
        """
        new_x = self.xcor() + self.x_move
        # if self.hit_wall():
        # change y direction of ball after a collision with wall
        # self.bounce()
        new_y = self.ycor() + self.y_move
        # self.setheading(self.heading()-5)
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        """change y direction of ball after a collision with wall"""
        self.y_move *= -1

    def bounce_x(self):
        """change x direction of ball after a collision with paddle
        or after an ended match (move ball towards the other player)"""
        self.x_move *= -1

    def hit_wall(self):
        """
        checks when ball hits top/bottom wall
        :return: True when the ball hits a wall, or False
        """
        if self.ycor() >= 280 or self.ycor() <= -280:
            return True
        return False

    def hit_paddle(self, paddles):
        """checks when ball hits a paddle"""
        # around 51 is the distance between the center of the paddle, and it's edge
        # (self.xcor() == 340 and self.distance(paddles[0]) < 65)
        if (self.xcor() == 340 and self.distance(paddles[0]) < 51) \
                or (self.xcor() == -340 and self.distance(paddles[1]) < 51):
            self.move_speed *= 0.9  # less delay, faster ball
            return True
        return False

    def paddle_misses(self):
        """checks if paddle misses the ball"""
        if self.xcor() > 390:
            return 0
        if self.xcor() < -390:
            return 1
        return -1

    def ball_reset(self):
        """reset ball pos and direction after an ended match"""

        self.goto(0, 0)
        # change x direction of ball
        self.bounce_x()
        self.move_speed = 0.07
