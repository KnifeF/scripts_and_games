import pandas as pd
from turtle import Turtle

N_STATES = 50


class States(Turtle):
    def __init__(self):
        """initialize States obj that represents us states game"""
        super().__init__(visible=False)
        self.correct_answers = 0
        self.states_data = None
        self.unfilled_states = []
        self.read_states_data()
        self.penup()

    def read_states_data(self):
        """reads states' data from a csv file using pandas library to a DataFrame,
        converts states' names to a list format"""
        # creates pandas DataFrame from a csv file
        self.states_data = pd.read_csv("50_states.csv", usecols=["state", "x", "y"])
        # a list of the values from a pandas series
        self.unfilled_states = self.states_data["state"].tolist()

    def is_correct_state(self, guess: str):
        """
        checks if user input is a correct state - increases correct answers number, and place the name on map
        :return: True for a correct guess, Otherwise False.
        """
        current_guess = guess.title()
        # checks if user guessed a correct state (a correct one should be within the list)
        if current_guess in self.unfilled_states:
            # remove correct guess from the list to avoid duplicate guesses
            self.unfilled_states.remove(current_guess)
            # increases correct guesses by one
            self.correct_answers += 1
            # place state name on it's defined position on window (bg image - represents a US map)
            self.place_state(state_name=current_guess)
            return True
        return False

    def place_state(self, state_name):
        """
        checks x,y pos of the state and place/write it on screen using turtle
        :param state_name: a state name to place on the map
        :return:
        """
        # pandas filter/query to find a row where a state called as given param,
        # and extract the values x, y as integers, in order to move turtle to required pos
        place_x = int(self.states_data[self.states_data["state"] == state_name]["x"])
        place_y = int(self.states_data[self.states_data["state"] == state_name]["y"])
        # print(states_data[states_data["state"] == "Alabama"])

        # move turtle to state's defined position on window (bg image - represents a US map)
        self.goto(x=place_x, y=place_y)
        # write the name of the state on screen when on it's defined position
        self.write(state_name)

    def has_all_states(self):
        """
        checks if user has answered all 50 states correctly.
        :return: True when a user answered 50 states correctly, Otherwise returns False.
        """
        if self.correct_answers < 50:
            return False
        return True

    def save_missed_states(self):
        """saves the states' names that the user missed from all 50 states
        to a CSV file using pandas"""
        # Creating a Dataframe with missed states' names
        missed_states_data = pd.DataFrame({"state": self.unfilled_states})
        # save df to a csv file
        missed_states_data.to_csv("states_to_learn.csv")

    # def save_unfilled_states(self):
    #     """saves the states that the user missed from all 50 states
    #     to a CSV file using pandas"""
    #     # Creating an empty Dataframe using relevant columns to hold states data
    #     missed_states_data = pd.DataFrame(columns=["state", "x", "y"])
    #     # for each missed state, use pandas filter to find its row and add to another DataFrame,
    #     # Then, save the DataFrame to a csv file
    #     for state_name in self.unfilled_states:
    #         state_row = self.states_data[self.states_data["state"] == state_name]
    #         missed_states_data = pd.concat([missed_states_data, state_row], ignore_index=True)
    #     missed_states_data.to_csv("missed_states.csv", index=False)
