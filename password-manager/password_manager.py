import re
# import pyperclip
import json
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox


# TODO-1: UI Setup, Tk Window, canvas and ordered widgets for password manager app
# TODO-2: get user data from entries and check for valid inputs
# TODO-3: Save user's data (website, email, password ) to a JSON file.
# TODO-4: Notify user with messagebox
# TODO-5: Generate a random password, copy saved password to clipboard
# TODO-6: Search a website in a JSON file, display account email and password with a popup

# Constants
EMAIL_STR = "example@gmail.com"
# email str pattern
# https://www.c-sharpcorner.com/article/how-to-validate-an-email-address-in-python/
# getting-pep8-invalid-escape-sequence-warning-trying-to-escape-parentheses-in-a
MAIL_PATTERN = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def reset_entries():
    """resets entries - delete text of website and password entries"""
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """generates a random password and returns as str"""
    password_list = []

    # adds random letters, symbols, and numbers (characters) to a list, using list comprehension
    password_list += [choice(LETTERS) for _ in range(randint(8, 10))]
    password_list += [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_list += [choice(NUMBERS) for _ in range(randint(2, 4))]

    # shuffle list to mix characters (in order to generate the password)
    shuffle(password_list)
    # Join all items in a list into a string
    password = "".join(password_list)
    print(f"Your password is: {password}")

    # Delete text from password entry
    password_entry.delete(0, END)
    # Insert generated password to password entry
    password_entry.insert(index=0, string=password)
    # Copy generated password to clipboard
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_mail_format(mail):
    """
    Validate an email address string pattern
    :param mail: a string to check if it's with email pattern
    :return: returning a Match for string with email pattern,
    or None if no match was found.
    """
    return re.search(pattern=MAIL_PATTERN, string=mail)


def valid_inputs(website: str, mail: str, password: str):
    """
    check user inputs
    :param website: a website (str)
    :param mail: a mail (str)
    :param password: a password (str)
    :return: True when the inputs are valid, otherwise False
    """
    # check valid inputs (from entries that the user filled)
    invalid_inputs = len(website) == 0 or len(mail) == 0 or len(password) == 0
    # Scan through string looking for a match to the pattern
    if invalid_inputs or not check_mail_format(mail=mail) or not website.isalnum():
        # notify user to fill details properly
        fill_properly_msg()
        return False
    return True


def load_credentials():
    """read credentials from json file"""
    with open(file="data.json", mode='r') as data_file:
        # reading from json file (old data)
        data = json.load(fp=data_file)
        return data


def save_credentials(data):
    """write credentials to json file"""
    with open(file="data.json", mode='w') as data_file:
        # write to json file (updated data)
        # Serialize obj as a JSON formatted stream to fp
        json.dump(obj=data, fp=data_file, indent=4)


def save_account_details():
    """Save website, user_email, and password to a file (adds to a JSON Format)"""
    # get text from entries
    website = website_entry.get().strip()
    mail = user_mail_entry.get().strip()
    password = password_entry.get().strip()
    # check user inputs
    if valid_inputs(website=website, mail=mail, password=password):
        # titlecased str
        website = website.title()

        # Ask if operation should proceed
        confirm_save = ok_to_save(website=website, mail=mail, password=password)
        if confirm_save:
            # dict with user data (from inputs)
            credentials_dict = {
                website: {
                    "email": mail,
                    "password": password
                }
            }

            # write website, mail, and password data to a json file
            try:
                # read credentials from json file to dict
                data = load_credentials()
            except FileNotFoundError:  # or json.decoder.JSONDecodeError as e:
                # print(f"{e}")
                save_credentials(data=credentials_dict)
            else:
                # update dict with new data
                data.update(credentials_dict)
                # write credentials to json file
                save_credentials(data=data)
            finally:
                # delete text from entries
                reset_entries()
                # Direct input focus to this widget
                website_entry.focus()
                # notify that login data is saved to file
                notify_saved()


# ---------------------------- SEARCH ACCOUNT CREDENTIALS ------------------------------- #

def search_website():
    """search the website from input within a text file in JSON format,
    and display account email and password with a popup"""
    website = website_entry.get().strip()
    if len(website) == 0 or not website.isalnum():
        return

    # titlecased str
    website = website.title()

    # read website, mail, and password data from a json file (to dict)
    try:
        credentials_dict = load_credentials()
    except FileNotFoundError:
        no_file_msg()  # an error message for website search
    else:
        # is a website name (str) exist in dictionary keys
        if website in credentials_dict.keys():
            try:
                # mail and password values within a dict key
                mail = credentials_dict[website]["email"]
                password = credentials_dict[website]["password"]
            except KeyError as e:
                print(f"key {e} is not exist")
            else:
                # display message with user credentials
                display_details_msg(website=website, mail=mail, password=password)
        else:
            no_details_msg(website=website)  # warning message that details are not found


# ---------------------------- messagebox ------------------------------- #
def notify_saved():
    """Notify the user that his website account data is saved to file"""
    # Show an info message (notify the user about saving account credentials to a file)
    messagebox.showinfo(title="Saving..", message="Successfully saved account details.")


def ok_to_save(website, mail, password):
    """
    Ask if operation should proceed to save data
    :param website: a website (str)
    :param mail: a mail (str)
    :param password: a password (str)
    :return: return True if the answer is ok
    """
    return messagebox.askokcancel(title=f"{website} account credentials",
                                  message=f"These are the details entered: \nEmail: {mail}"
                                          f"\nPassword: {password} \nIs it ok to save?")


def fill_properly_msg():
    """Message to notify user to fill details properly"""
    messagebox.showwarning(title=f"Oops",
                           message=f"Please fill the details properly without leaving empty fields.")


def no_file_msg():
    """Error Message to notify user that the file is not found"""
    messagebox.showerror(title="Error", message="No Data File Found.")


def no_details_msg(website: str):
    """warning message that details are not found in JSON file"""
    messagebox.showwarning(title="Error", message=f"No details for {website} exists")


def display_details_msg(website, mail, password):
    """
    show user credential for a given website str
    :param website: a website (str)
    :param mail: a mail (str)
    :param password: a password (str)
    :return:
    """
    messagebox.showinfo(title=f"{website}",
                        message=f"Email: {mail}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
# widget of Tk as the main window of an application
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Construct and position a canvas widget, create an image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# add and position relevant widgets, labels, entries, buttons
# Labels
website_label = Label(text="Website:")
user_mail_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1)
user_mail_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# sticky=NSEW - if cell is larger on which sides will this widget stick to the cell boundary
# sticky="EW" to fix widgets alignment (entries/buttons)
# Entries
website_entry = Entry(width=45)
user_mail_entry = Entry(width=45)
password_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()  # Direct input focus to this widget.
user_mail_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
user_mail_entry.insert(index=0, string=f"{EMAIL_STR}")
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
search_button = Button(text="Search", command=search_website)
gen_pass_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=save_account_details)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
gen_pass_button.grid(column=2, row=3, sticky="EW")
search_button.grid(column=2, row=1, sticky="EW")

# loop of the application window which runs so that we can see the still screen
window.mainloop()
