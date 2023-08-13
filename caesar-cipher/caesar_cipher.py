from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        # TODO-3: Keep the number/symbol/space when the text is encoded/decoded
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if "a" <= char <= "z":
            position = alphabet.index(char)
            new_position = position + shift_amount

            if new_position >= len(alphabet):
                end_text += alphabet[new_position - len(alphabet)]
            else:
                end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
print(logo)

# TODO-4: ask the user if they want to restart the cipher program
# Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the 'caesar' function again
running_cipher = True

while running_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: the program should work even if the user enters a shift number greater than 26,
    #  number of letters in the alphabet (using modulus)
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart_cipher = input(
        "Do you want to restart the cipher program.\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart_cipher.lower() == "no" or restart_cipher == "n".lower():
        running_cipher = False
