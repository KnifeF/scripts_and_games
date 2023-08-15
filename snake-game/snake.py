from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SNAKE_COLOR = "#80ce87"


class Snake:
    def __init__(self):
        """Initializes a Snake obj"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Creates the snake body (first 3 segments)
        """
        for position in STARTING_POSITIONS:
            self.add_segment(seg_pos=position)

    def add_segment(self, seg_pos):
        """
        adds a segment to snake's body
        :param seg_pos: given segment position
        :return:
        """
        # creates a Turtle obj, as a snake body part
        new_segment = Turtle(shape="square")
        new_segment.color(SNAKE_COLOR)  # pencolor
        new_segment.speed("fastest")  # turtle's speed
        # Pull the pen up – no drawing when moving.
        new_segment.penup()
        # Move turtle to an absolute position.
        new_segment.goto(seg_pos)
        # add a snake segment (body part/tail) to a list,
        # that represents the snake segments (whole body)
        self.segments.append(new_segment)

    def move(self):
        """moving the snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # current segment goto position of the next segment (first segment of list is snake's head)
            next_pos = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(next_pos)
        # Move the turtle forward by the specified distance - moves snake's head forward
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        """checks current heading of snake's head. move the snake right"""
        if self.head.heading() not in (RIGHT, LEFT):
            self.head.setheading(RIGHT)

    def up(self):
        """checks current heading of snake's head. move the snake up"""
        if self.head.heading() not in (UP, DOWN):
            self.head.setheading(UP)

    def left(self):
        """checks current heading of snake's head. move the snake left"""
        if self.head.heading() not in (RIGHT, LEFT):
            self.head.setheading(LEFT)

    def down(self):
        """checks current heading of snake's head. move the snake down"""
        if self.head.heading() not in (UP, DOWN):
            self.head.setheading(DOWN)

    def increase_len(self):
        """Snake grows body length/tail after eating food"""
        # position of snake's tail (position of last segments in the snake body/list)
        tail_position = self.segments[-1].position()
        # add a new segment to snake's body/tail after eating food
        self.add_segment(tail_position)

    def detect_hit_wall(self):
        """
        Checks for a collision of snake's head with the walls. The edges of the screen called walls.
        :return: True - when snake's head hit a wall (-280/280, y), (x, -280/280). Otherwise - False.
        """
        # turtle's x and y coordinates.
        head_x = self.head.xcor()
        head_y = self.head.ycor()
        # bool checks if snake's head hit a wall (-300/300, y), (x, -300/300)
        collision_x_edge = head_x < -290 or 290 < head_x
        collision_y_edge = head_y < -290 or 290 < head_y
        return collision_x_edge or collision_y_edge

    def eat_itself(self):
        """
        Checks for a collision of snake's head with snake's tail.
        :return: True - when snake's head hits other parts/the tail of the snake. Otherwise - False.
        """
        # bool checks if snake's head hits other parts of the snake
        for seg_num in range(len(self.segments) - 1, 1, -1):
            # head's distance from a tail part is lower than 10, so the snake probably hits tail
            if self.head.distance(self.segments[seg_num]) < 10:
                return True
        return False
