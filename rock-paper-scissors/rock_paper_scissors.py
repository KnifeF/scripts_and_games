from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

you_win = '''
+-+-+-+ +-+-+-+
|Y|o|u| |w|i|n|
+-+-+-+ +-+-+-+
'''
you_lose = '''
+-+-+-+ +-+-+-+-+
|Y|o|u| |l|o|s|e|
+-+-+-+ +-+-+-+-+                         
'''
a_draw = '''
+-+-+-+ +-+ +-+-+-+-+
|I|t|s| |a| |d|r|a|w|
+-+-+-+ +-+ +-+-+-+-+
'''

usr_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
rand_choise = randint(0, 2)

if (usr_input == "0" or usr_input == "1" or usr_input == "2"):
    hand = int(usr_input)

    # list of strings that represent rps hands in ascii-art
    rps_lst = [rock, paper, scissors]

    # nested List that contain strings (ascii arts) for wining, losing or a draw results in rps
    # 0 for Rock, 1 for Paper or 2 for Scissors
    # eg: [0][2] points to a situation when you have Rock(0), and the computer has Scissors(2), so you win..
    rps_result_matrix = [[a_draw, you_lose, you_win],
                         [you_win, a_draw, you_lose],
                         [you_lose, you_win, a_draw]]

    # prints "ascii arts" that represent your "rps" hand, and computer's random "rps" hand
    # then the result of the game (win/lose/a draw)
    print(f"{rps_lst[hand]}\nComputer chose:\n{rps_lst[rand_choise]}\n{rps_result_matrix[hand][rand_choise]}")

else:
    print("invalid input!")
