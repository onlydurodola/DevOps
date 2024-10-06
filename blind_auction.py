#we working
# TODO-1: Ask the user for input 
import os

import art

print(art.logo)


def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS/Linux
        os.system('clear')


clear_screen()

information = {}
loop = True
while loop:

    name = input("What is your name?: ").lower()
    bid = input("What is your bid?: $")
    depends = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if depends != "yes" and depends != "no":
        print("Wrong entry, try again.")

    clear_screen()
    information[name] = int(bid)

    if depends == "no":
        loop = False

max_bid = max(information.values())
max_key = max(information, key=information.get)

print(f"The winner of this bid is {max_key} with a bid of ${max_bid}")

# get_highest = str(0)
# keys = ""
# for info in information:
#     if info > get_highest:


# def clear_screen():
#     # For Windows
#     if os.name == 'nt':
#         os.system('cls')
#     # For Linux/macOS
#     else:
#         os.system('clear')


# clear_screen()

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
