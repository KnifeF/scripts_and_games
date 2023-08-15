from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_HEADING = 180


class Car(Turtle):
    def __init__(self):
        """initializes a Car obj"""
        super().__init__(shape="square")
        # Pull the pen up – no drawing when moving.
        self.penup()
        # Set turtle's stretchfactors/outline. 40*20 px
        self.shapesize(stretch_wid=1, stretch_len=2)
        # turtle's color (random color from a list)
        self.color(random.choice(COLORS))
        # Set the orientation of the turtle to to_angle.
        self.setheading(CARS_HEADING)
        # set a random position
        self.rand_pos()

    def rand_pos(self):
        """sets random position for a generated car"""
        rand_y = random.randint(-250, 250)
        self.goto(x=300, y=rand_y)


class CarManager:
    def __init__(self):
        """initializes a CarManager obj"""
        # list of cars
        self.cars = []
        # move distance/current speed for cars
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        """creates a car and appends to a list of cars"""
        self.cars.append(Car())

    def move_cars(self):
        """moves the cars forward"""
        for a_car in self.cars:
            a_car.forward(self.move_distance)

    def increase_speed(self):
        """increases cars' speed/move distance"""
        self.move_distance += MOVE_INCREMENT
