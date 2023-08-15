from turtle import Turtle

STARTING_POSITION = (0, -280)
START_HEADING = 90
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        # Pull the pen up – no drawing when moving.
        self.penup()
        # reset the position of the turtle
        self.reset_position()

    def walk(self):
        """A turtle moves forwards when you press the 'Up' key"""
        self.forward(distance=MOVE_DISTANCE)

    def reach_finishline(self):
        """turtle reaches th finish line"""
        return self.ycor() >= FINISH_LINE_Y

    def reset_position(self):
        """reset the position of the turtle to the start of the cross"""
        self.goto(STARTING_POSITION)
        self.setheading(START_HEADING)

    def hit_car(self, cars):
        """When the turtle collides with a car, it's game over and everything stops."""
        # a_car.xcor() + 10
        for a_car in cars:
            # if abs(self.ycor() - a_car.ycor()) < 20 and abs(self.xcor() - a_car.xcor()) < 30:
            # if abs(self.ycor() - a_car.ycor()) <= 10 and self.distance(a_car) <= 18:
            if self.distance(a_car) < 20:
                return True
        return False
