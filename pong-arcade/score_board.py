import sys
from turtle import Turtle
from time import sleep

FONT = ("Lucida Console", 40, "normal")
CENTER = "center"
SCORE_COLOR = "#BBA14F"


class ScoreBoard(Turtle):
    def __init__(self):
        """Initializes a ScoreBoard obj"""
        super().__init__(visible=False)
        self.right_score = 0
        self.left_score = 0
        self.game_is_on = True
        # Pull the pen up – no drawing when moving.
        self.penup()
        # set color
        self.color(SCORE_COLOR)
        # Move turtle to an absolute position.
        # self.goto(x=0, y=260)
        self.goto(x=0, y=240)
        # Displays updated score on screen.
        self.display_score()

    def display_score(self):
        """Displays updated score on screen. Writes score as text."""
        # Delete the turtle's drawings from the screen.
        self.clear()
        # out_score = f"Player 2: {self.left_score} |VS| Player 1: {self.right_score}"
        out_score = f"{self.left_score} |VS| {self.right_score}"
        self.write(out_score, align=CENTER, font=FONT)

    def add_a_point(self, winner_status: int):
        """
        increases score of the player that won a match
        :param winner_status: 0 represents player2, 1 represents player1 win the match
        :return:
        """
        if winner_status == 0:
            self.left_score += 1
        else:
            self.right_score += 1
        self.display_score()

    def quit(self):
        """
        Quit the game
        :return:
        """
        self.clear()  # clear the screen
        out_msg = f"Bye bye 😎🙏"
        self.write(out_msg, align=CENTER, font=FONT)  # print by msg
        sleep(2)  # short delay
        self.game_is_on = False
