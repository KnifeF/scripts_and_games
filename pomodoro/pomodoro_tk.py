import math
from tkinter import *

# TODO-1: Setup canvas widget and add images
# TODO-2: Pomodoro UI Setup with Tkinter, and relevant widgets
# TODO-3: Handle Timer - start/reset/countdown mechanism

# ---------------------------- CONSTANTS ------------------------------- #
# colors and fonts
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SMALL_FONT = (FONT_NAME, 12)
COUNTDOWN_FONT = (FONT_NAME, 35, "bold")
TIMER_FONT = (FONT_NAME, 50)

# TIME FOR SESSIONS IN MIN
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

# Unicode Character “🍅” (U+1F345) - tomato
TOMATO_CHAR = "🍅"

reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """reset the pomodoro timer"""
    global timer, reps
    if timer:
        # Cancel scheduling of function identified with ID.
        window.after_cancel(timer)
        # reset the countdown text (to 00:00)
        canvas.itemconfig(timer_text, text=f"00:00")
        # resets label text (to "Timer")
        timer_label.config(text="Timer")
        # clears the pomodoros marks from text
        pomodoro_count_label.config(text="")
        # set reps back to zero
        reps = 0
        # reset/enable the start button
        start_button.config(state=NORMAL)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """
    start counting working sessions
    :return:
    """
    global reps

    # https://www.codershubb.com/prevent-the-tkinter-buttons-from-multiple-clicks/
    # disable the start button to avoid another click during a session
    start_button.config(state=DISABLED)

    # increases reps each time the func is called
    reps += 1

    # time in sec for work/short break/long break
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # a long break
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        # a short break
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        # a working session
        timer_label.config(text="Work", fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    """countdown to zero and update time remaining for the text on canvas"""
    global reps, timer  # , is_reset_clicked, start_clicked
    # convert seconds remaining to a min:sec format
    minutes = math.floor(count / 60)
    seconds = math.floor(count % 60)

    # adds a zero in case the number is less than 10 (only 1 digit)
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"

    # update text in canvas - countdown state (min:sec)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        # still countdown current work/break session
        # Call function once after given time (in milliseconds)
        timer = window.after(1000, countdown, count - 1)
    else:
        if reps == 8:
            # reset timer after repeating 8 work-break sessions, in order to remove pomodoro marks,
            # and to start pomodoro tracking from zero
            # (25min, 5min , 25min, 5min, 25min, 5min, 25min, 20min)
            reset_timer()

        # starts the next work/break countdown
        start_timer()

        # add pomodoro marks to label text (for num of completed work sessions)
        tomato_count = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(0, work_sessions):
            tomato_count += TOMATO_CHAR
        pomodoro_count_label.config(text=tomato_count)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# title of this widget.
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label widget as timer title
timer_label = Label(text="Timer", font=TIMER_FONT, fg=GREEN, bg=YELLOW)

# Construct a canvas widget with the parent MASTER
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Create an image and add to canvas (tomato image)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
# Create text with coordinates x, y, using specific color and font
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=COUNTDOWN_FONT)

# add buttons for timer start/reset
start_button = Button(text="Start", font=SMALL_FONT, command=start_timer)
reset_button = Button(text="Reset", font=SMALL_FONT, command=reset_timer)

# label to keep track pomodoro marks (work sessions)
pomodoro_count_label = Label(text="", font=(FONT_NAME, 16, "bold"), fg=RED, bg=YELLOW)

# Position the labels, buttons, and canvas
timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
pomodoro_count_label.grid(row=3, column=1)
reset_button.grid(row=2, column=2)

# loop of the application window which runs so that we can see the still screen
window.mainloop()
