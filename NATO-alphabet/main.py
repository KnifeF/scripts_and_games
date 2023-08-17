import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# Creates a pandas DataFrame from a csv file
nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# create a dictionary (letter, phonetic code) from a DataFrame
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# ask for a word input
word_input = input(f"Enter a word: ")
# Create a list of relevant phonetic code
phonetic_code_words = [nato_alphabet_dict[letter.upper()] for letter in word_input]
print(phonetic_code_words)
