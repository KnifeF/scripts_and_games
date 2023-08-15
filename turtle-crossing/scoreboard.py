from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        # set color
        self.color("black")
        # Pull the pen up – no drawing when moving.
        self.penup()
        # current level
        self.level = 1

    def next_level(self):
        """increases level"""
        self.level += 1

    def display_level(self):
        """display level on screen"""
        # Delete the turtle's drawings from the screen.
        self.clear()
        # Move turtle to an absolute position.
        self.goto(x=-200, y=240)
        # Write text at the current turtle position.
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_ended(self):
        """display game over on screen"""
        # Move turtle to an absolute position.
        self.goto(0, 0)
        # Write text at the current turtle position.
        self.write("Game Over!", align="center", font=FONT)
