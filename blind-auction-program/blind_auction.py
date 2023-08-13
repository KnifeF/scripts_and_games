from art import logo


def find_highest_bid(bids):
    # Find the highest bid in the dictionary and declare them as the winner
    highest_bid = 0
    higher_bidder_name = ""

    for bidder in bids:
        current_bid = int(bids[bidder])
        if current_bid > highest_bid:
            highest_bid = current_bid
            higher_bidder_name = bidder

    print(f"The winner is {higher_bidder_name}, with a bid of ${highest_bid}.")


# TODO-1: Show logo from art.py
print(logo)

blind_auction_bids = {}
waiting_bidders = True
while waiting_bidders:
    # TODO-2: Ask for Name input and Bid Price
    print("Welcome to the secret auction program.")
    name = input("Please Enter Your Name: ")
    bid = input("Please Enter Your Bid: $")

    # TODO-3: Add Name and Bid into a dictionary as the key and value.
    blind_auction_bids[name] = bid

    # TODO-4: Ask if there are other users who want to bid.
    # For "yes", Clear the screen. For "no" Find the highest bid in the dictionary and declare them as the winner
    user_answer = input("Are there other bidders? Answer 'Yes' or 'No': ")
    if user_answer.lower() != "yes":
        waiting_bidders = False
    # if user_answer.lower() == "yes":
    # call clear() to clear the output in the console.
    #     clear()
    # else:
    #     waiting_bidders = False
    # elif user_answer.lower() == "no":
    # waiting_bidders == False

# print(blind_auction_bids, "\n")

# TODO-5: Find the highest bid in the dictionary and declare them as the winner
find_highest_bid(blind_auction_bids)
