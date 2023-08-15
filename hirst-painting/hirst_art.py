# import colorgram
import turtle
import random

'''
# The Hirst Painting Project - 1. extract rgb values from images
def extract_colors(img_name, n_of_colors):
    """
    extracts N colors from an image using colorgram library
    :param n_of_colors: num of colors to extract
    :type img_name: str
    :return 30 rgb colors, that are extracted from given image (list)
    """
    # Extract 30 colors from an image.
    # colors = colorgram.extract(img_name, 30)

    # colorgram - A Python module for extracting colors from images. Get a palette of any picture!
    # Extract N colors from an image.
    colors = colorgram.extract(img_name, n_of_colors)

    rgb_colors = []
    for color in colors:
        # Color.rgb - The color represented as a namedtuple of RGB from 0 to 255, e.g. (r=255, g=151, b=210)
        current_color = (color.rgb.r, color.rgb.g, color.rgb.b)
        rgb_colors.append(current_color)  # Append tuple to the end of the list.
    return rgb_colors


# colors_list = extract_colors('hirst_work.jpg')
colors_list = extract_colors('damien_hirst_spots.jpg', 35)
'''

# https://en.wikipedia.org/wiki/Damien_Hirst


# The Hirst Painting Project - 2. drawing the dots
def make_hirst_style_art(raw_dots, column_dots, dots_size):
    """
    draw N dots, with gaps between them (same distance), and using some random colors
    :param column_dots: num of dots in a columns to be painted
    :param raw_dots: num of dots in a raw to be painted
    :param dots_size: size of the dots that are painted
    :return:
    """
    # Return the turtle's x coordinate.
    start_x = tim.xcor() - 200
    # Return the turtle's y coordinate.
    current_y = tim.ycor() - 200
    tim.setposition((start_x, current_y))  # Move turtle to an absolute position.

    for i in range(raw_dots):
        for j in range(column_dots):
            # Draw a dot with diameter size, using random color
            tim.dot(dots_size, random.choice(colors_for_painting))
            tim.forward(50)

        current_y += 50  # increases y pos value
        # Move turtle to an absolute position.
        tim.setposition((start_x, current_y))


# list with some colors for the art
colors_for_painting = [(216, 152, 82), (48, 94, 140), (129, 167, 192), (151, 59, 69), (133, 73, 55),
                       (236, 209, 85), (216, 69, 91), (217, 79, 60), (28, 33, 54), (200, 139, 155),
                       (58, 33, 20), (26, 131, 88), (128, 188, 162), (50, 54, 100), (58, 27, 36),
                       (104, 42, 53), (37, 169, 202), (47, 166, 136), (151, 179, 58), (242, 210, 4),
                       (236, 172, 159), (23, 59, 37), (160, 207, 181), (94, 124, 176), (64, 77, 34),
                       (223, 172, 183), (107, 43, 41), (154, 205, 210), (9, 112, 68), (181, 187, 210),
                       (8, 96, 114)]
# print(colors_for_painting)

turtle.colormode(255)  # sets color mode

tim = turtle.Turtle()  # turtle obj
tim.speed("fastest")  # sets the turtle's speed.
tim.hideturtle()  # Makes the turtle invisible.
tim.penup()  # Pull the pen up – no drawing when moving.

# draw some damien hirst style art on screen
make_hirst_style_art(raw_dots=random.randint(5, 11), column_dots=random.randint(5, 11),
                     dots_size=random.randint(10, 21))

screen = turtle.Screen()  # a screen obj
screen.exitonclick()  # Go into mainloop until the mouse is clicked.
