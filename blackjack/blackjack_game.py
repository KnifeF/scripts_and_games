from random import choice
from art import logo, ascii_cards

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# TODO-1: Create a deal_card() function
def deal_card():
    """
    return a random card (int) from a list
    """
    return choice(cards)


# TODO-2: Deal the user and computer 2 cards
def deal():
    """
    Deal the user and computer 2 cards each
    """
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    return user_cards, computer_cards


# TODO-3: Create a function called calculate_score()
def calculate_score(cards):
    """
    takes a List of cards as input and returns the score, or 0 that represent a blackjack in our game, or -1 that
    represent a bust (over 21)
    """
    # Calculate user's or computer's scores based on their card values.
    score = sum(cards)
    if score == 21:
        return 0
    if score > 21:
        if 11 in cards:
            # If an ace is drawn, count it as 11. But if the total goes over 21,
            # count the ace as 1 instead.
            cards.remove(11)
            cards.append(1)
        else:
            return -1
    return sum(cards)


# TODO-7: Create a function called compare()
def compare(user_score, computer_score):
    """
    Compares user and computer scores and see if it's a win, loss, or draw.
    """
    # Detect when computer or user has a blackjack. (Ace + 10 value card).
    if computer_score == 0:
        # If computer gets blackjack, then the user loses (even if the user also has a blackjack).
        return "Computer has a Blackjack! You Lose."
    if user_score == 0:
        # If the user gets a blackjack, then they win (unless the computer also has a blackjack).
        return "Blackjack! You Win."
    if user_score == -1:
        return "You have a Bust! You Lose."
    if computer_score == -1:
        return "Computer has a Bust! You Win."
    if user_score == computer_score:
        return "It's a Draw."
    if user_score > computer_score:
        return "You Win."
    return "You Lose."


def conv_card_to_ascii(card):
    """
    takes a card (int) as input and return card in converted 'ascii art' form (string)
    """
    if card == 11 or card == 1:
        # ascii str that represent an ace
        return ascii_cards[0]
    elif card == 10:
        # ascii str that represent 10/J/Q/K (random choice between them)
        # sublist in a list
        # https://stackoverflow.com/questions/13187619/sublist-in-a-list
        ten_jqk = ascii_cards[9:12]
        return choice(ten_jqk)
    else:
        # append to list a string (that represent a card from 2-9 that within given list)
        return ascii_cards[card - 1]


def display_ascii_cards(cards_to_display):
    """
    takes a list (of strings) that holds ascii representation of cards,
    then prints lines in ordered way to console so user could see the cards
    """
    ascii_display = ""  # a string to display the ascii cards ordered one by one for the viewer

    # each card str has 4 lines. loop over each line.
    for i in range(4):
        # iterates over list of strings that represent ascii cards
        # ascii_display +=  "  "
        for j in range(len(cards_to_display)):
            # represent an ascii cards
            current_ascii_card = cards_to_display[j]
            # split lines of an ascii cards and removes empty lines (using sublist)
            splited_card_lines = current_ascii_card.split("\n")[1:-1]
            # string concatenation between specific cards' lines,
            # and order them one by one for the viewer  when they are displayed on console
            ascii_display += splited_card_lines[i] + "  "
        ascii_display += "\n"

    print(ascii_display)


def play_blackjack():
    """
    runs a game of blackjack
    """
    print(logo)  # prints logo of the game (ascii art - str)

    # Deal both user and computer a starting hand of 2 random card values (2 lists of integers).
    user_cards, computer_cards = deal()

    # lists of str with an ascii representation of cards
    user_cards_in_ascii = []
    computer_cards_in_ascii = []

    # convert list (of int) that represent cards to list (of str) that represent ascii cards (more graphical)
    for crd in user_cards:
        user_cards_in_ascii.append(conv_card_to_ascii(crd))
    for crd in computer_cards:
        computer_cards_in_ascii.append(conv_card_to_ascii(crd))

    # TODO-4: Call calculate_score()
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # show the user it's hand (current state of his cards)
    # print(f"Your cards: {user_cards}. Score: {user_score}")
    print("Your cards:")
    display_ascii_cards(user_cards_in_ascii)
    print(f"Score: {user_score}")

    # Reveal computer's first card to the user.
    # print(f"computer's first card: {computer_cards[0]}")
    print("computer's first card:")
    display_ascii_cards([computer_cards_in_ascii[0]])

    # Game ends immediately when user score goes over 21,
    # or if the user or computer gets a blackjack.
    game_state = compare(user_score, computer_score)
    round_ends = False
    if "blackjack" in game_state.lower() or "you have a bust" in game_state.lower():
        # print(game_state)
        round_ends = True

    # Game has not ended immediately
    if not round_ends:
        stop_dealing = False
        # Ask the user if they want to get another card.
        while (not stop_dealing) and (not round_ends):
            another_card = input("Do you want to get another card? y/n: ")
            if another_card.lower() == "y" or another_card.lower() == "yes":
                crd = deal_card()  # get another card
                user_cards.append(crd)

                # convert new given card from int representation to str (ascii) and adds to list
                user_cards_in_ascii.append(conv_card_to_ascii(crd))

                # TODO-6: The score will need to be rechecked with every new card drawn
                user_score = calculate_score(user_cards)

                # show the user it's hand (current state of his cards)
                # print(f"Your cards: {user_cards}. Score: {user_score}")
                print("Your cards:")
                display_ascii_cards(user_cards_in_ascii)
                print(f"Score: {user_score}")

                # Reveal computer's first card to the user.
                # print(f"computer's first card: {computer_cards[0]}")
                print("computer's first card:")
                display_ascii_cards([computer_cards_in_ascii[0]])

                game_state = compare(user_score, computer_score)
                if "you have a bust" in game_state.lower():
                    round_ends = True
                elif "blackjack" in game_state.lower():
                    stop_dealing = True
            else:
                # Once the user is done and no longer wants to draw any more cards, let the computer play.
                stop_dealing = True

        # TODO-6: The computer should keep drawing cards as long as it has a score less than 17.
        # Once the user is done and no longer wants to draw any more cards, let the computer play.
        # The computer should keep drawing cards unless their score goes over 16.
        if stop_dealing and not round_ends:
            while 0 < computer_score < 17:
                crd = deal_card()  # get another card
                computer_cards.append(crd)

                # convert new given card from int representation to str (ascii) and adds to list
                computer_cards_in_ascii.append(conv_card_to_ascii(crd))

                computer_score = calculate_score(computer_cards)

                game_state = compare(user_score, computer_score)
                lower_state = game_state.lower()
                if "computer" in lower_state and ("blackjack" in lower_state or "bust" in lower_state):
                    break

    # Compare user and computer scores and see if it's a win, loss, or draw.
    game_state = compare(user_score, computer_score)
    print("\n", game_state)

    # Print out the player's and computer's final hand and their scores at the end of the game.
    # print(f"Your cards: {user_cards}. Score: {sum(user_cards)}")
    print("Your cards:")
    display_ascii_cards(user_cards_in_ascii)
    print(f"Score: {sum(user_cards)}")

    # print(f"Computer's cards: {computer_cards}. Computer's score: {sum(computer_cards)}")
    print("Computer's cards:")
    display_ascii_cards(computer_cards_in_ascii)
    print(f"Computer's score: {sum(computer_cards)}")

    # After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
    print("*************************************")
    want_game = input("Do you want to play BlackJack? y / no: ")
    if want_game.lower() == "y" or want_game.lower() == "yes":
        print("\n\n\n")
        play_blackjack()


play_blackjack()
