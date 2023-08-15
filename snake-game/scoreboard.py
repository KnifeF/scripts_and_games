from turtle import Turtle

# FONT = ("Courier", 12, "bold")
FONT = ("Lucida Console", 12, "normal")
LOSER_FONT = ("Courier", 16, "bold")
CENTER = "center"
GAME_OVER = "GAME OVER!"
HIT_WALL = "HIT THE WALL."
HIT_TAIL = "HIT YOUR TAIL."


class Scoreboard(Turtle):
    def __init__(self):
        """Initializes a Scoreboard obj"""
        super().__init__(visible=False)
        self.total_score = 0
        # Pull the pen up – no drawing when moving.
        self.penup()
        # set pencolor to red
        self.color("#22b455")
        # Move turtle to an absolute position.
        self.goto(x=0, y=260)
        # Displays updated score on screen.
        self.display_score()

    def display_score(self):
        """Displays updated score on screen. Writes score as text."""
        # Delete the turtle's drawings from the screen.
        self.clear()
        out_score = f"Score: {self.total_score}"
        # if wall:
        #     out_score += f"\n{GAME_OVER} {HIT_WALL}"
        # elif tail:
        #     out_score += f"\n{GAME_OVER} {HIT_TAIL}"
        # Write text at the current turtle position.
        self.write(out_score, align=CENTER, font=FONT)

    def game_over(self, wall=False, tail=False):
        """
        Displays game over text on screen. Writes relevant output when snake
        hits a wall, or it's tail
        :param wall:
        :param tail:
        :return:
        """
        lose_out = f"{GAME_OVER}\n"
        if wall:
            lose_out += HIT_WALL
        elif tail:
            lose_out += HIT_TAIL
        # goto center of screen
        self.goto(0, 0)
        # Write text at the current turtle position.
        self.write(lose_out, align=CENTER, font=LOSER_FONT)

    def increase_score(self, score_val):
        """
        increases total score by given score
        :param score_val: score to add and increase total score
        :return:
        """
        self.total_score += score_val
        # Displays updated score on screen.
        self.display_score()
