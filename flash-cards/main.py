"""Flash Card - learn the most frequently used words in given language.

For each round a Flash Card shows a word on the front and a translation on the back side of it.
After 3 seconds, the card flips, so the user should be able to check whether he knew the right translation.
If he knows it right he will press the checkmark. Otherwise, he will press the cross button.

Using Tkinter for Flash Card UI, pandas to read/write words' data in csv file.

note: the csv file has to include a specific format (2 columns - one for each language),
so the program will work properly:

first_language,second_language
word,translated_word
...
e.g:
French,English
partie,part
histoire,history
chercher,search
seulement,only
police,police
pensais,thought
"""
import sys
import pandas as pd
from tkinter import *
from random import choice

# from pandas.errors import ParserError, EmptyDataError
# except (FileNotFoundError, ParserError, EmptyDataError, ValueError) as e:
# https://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block

# 3 sec in milliseconds
WAIT = 3000
# colors/fonts
BACKGROUND_COLOR = "#B1DDC6"
BLACK = "black"
WHITE = "white"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
# paths
WORDS_PATH = "data/french_words.csv"
TO_LEARN_PATH = "data/words_to_learn.csv"
CARD_BACK = "images/card_back.png"
CARD_FRONT = "images/card_front.png"
CHECKMARK_OPT = "images/right.png"
CROSS_OPT = "images/wrong.png"

# TODO-1: Create the User Interface (UI) with Tkinter (widgets, fonts, measurements, and positioning)
# TODO-2: Get words' data from csv file (word/translation of 2 languages, e.g: bureau --> office)
# TODO-3: Create new flash cards with word/translation data.
# TODO-4: Display a random word on card's front, and the card flips to show the translation.
# TODO-5: The user should choose the checkmark button when he knows the translation.
#  Otherwise, he should choose the cross button.
# TODO-6: When user choose the checkmark, the word will be removed from the data, to avoid repeated test
# TODO-7: Words/translation to learn (that the user does not know) are saved to a csv file.

# read word/translation data from csv file (to pandas DataFrame).
df = None
try:
    df = pd.read_csv(TO_LEARN_PATH, dtype=str)
except (FileNotFoundError, ValueError) as e:
    try:
        df = pd.read_csv(WORDS_PATH, dtype=str)
    except (FileNotFoundError, ValueError) as e:
        sys.exit(e)

if not isinstance(df, pd.DataFrame):
    sys.exit()

# extract two languages from df columns
# e.g: French,English
try:
    from_language = df.columns.to_list()[0]
    to_language = df.columns.to_list()[1]
except IndexError as e:
    sys.exit(e)

# Get the words/translation rows from DataFrame as a list of dictionaries.
# represent a list of dictionaries with word/translation details for flash cards
words_to_learn = df.to_dict(orient="records")
# represent a dict with current flash card details
# e.g.: {'French': 'aucun', 'English': 'no'}
current_card = {}


# ---------- handle triggered buttons, flash card/translations, words to learn ---------- #
def clicked_known():
    """triggered when the user clicks on the checkmark_button when he knows the translation,
    and saves words' data to a csv files"""
    try:
        # Remove first occurrence of value
        words_to_learn.remove(current_card)
    except ValueError:
        sys.exit("ValueError: list.remove(x): x not in list")
    # save known words translations to a csv file using pandas
    known_words_df = pd.DataFrame.from_records(data=words_to_learn)
    known_words_df.to_csv(TO_LEARN_PATH, index=False)
    # move to next flash card
    next_card()


def next_card():
    """move to next random card (and display)"""
    global current_card, cancel_id

    if cancel_id:
        # Cancel scheduling of function identified with ID.
        window.after_cancel(id=cancel_id)

    try:
        # a new random word/translation (a dict) from list of dictionaries
        current_card = choice(words_to_learn)
    except IndexError:
        sys.exit()

    # flip flash card to the front
    show_front()
    # After a delay of 3s, the card flips to display the translation (show_back func).
    cancel_id = window.after(ms=WAIT, func=show_back)


def show_front():
    """flip flash card to the front - update image to card's front,
    and the text in canvas to the word (and language)"""
    # The card image should change to the card_front.png
    canvas.itemconfig(card_image, image=front_image)
    # The title of the card should change to the given language (str)
    canvas.itemconfig(title_text, text=from_language, fill=BLACK)
    # shows text of word. text colour should change to black.
    canvas.itemconfig(word_text, text=current_card[from_language], fill=BLACK)


def show_back():
    """flip flash card to the back - update image to card's back,
    and the text in canvas to the translated word (and language)"""
    # The card image should change to the card_back.png
    canvas.itemconfig(card_image, image=back_image)
    # The title of the card should change to translation's language (str)
    canvas.itemconfig(title_text, text=to_language, fill=WHITE)
    # shows text of translated word. text colour should change to white.
    canvas.itemconfig(word_text, text=current_card[to_language], fill=WHITE)


# Tk flash cards for word-translation knowledge test
# ------------ Setup UI with tkinter ------------ #
# Tk window
window = Tk()
window.title(string="Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# var to hold identifier to cancel scheduling of func with after_cancel
cancel_id = window.after(WAIT, func=show_back)

try:
    # Create Widgets which can display images (PhotoImage)
    front_image = PhotoImage(file=CARD_FRONT)
    back_image = PhotoImage(file=CARD_BACK)
    cross_image = PhotoImage(file=CROSS_OPT)
    checkmark_image = PhotoImage(file=CHECKMARK_OPT)
except TclError as e:
    sys.exit(e)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# create image and texts for the canvas
card_image = canvas.create_image(400, 263, image=front_image)  # (400, 263: center of the window pos)
title_text = canvas.create_text(400, 150, text="", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)

# Buttons with images (checkmark, cross)
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
checkmark_button = Button(image=checkmark_image, highlightthickness=0, command=clicked_known)

# Position a widget in the parent widget in a grid
canvas.grid(column=0, row=0, columnspan=2)
cross_button.grid(row=1, column=0)
checkmark_button.grid(row=1, column=1)

next_card()  # move to next random card

window.mainloop()  # Call the mainloop of Tk.
