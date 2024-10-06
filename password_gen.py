import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# random.shuffle(letters)
# random.shuffle(numbers)
# random.shuffle(symbols)

choice_let = []
for letter in range(0, nr_letters):
    choice_let.append(random.choice(letters))

choice_symbol = []
for symbol in range(0, nr_symbols):
    choice_symbol.append(random.choice(symbols))

choice_numbers = []
for number in range(0, nr_numbers):
    choice_numbers.append(random.choice(numbers))

new_list = choice_let + choice_numbers + choice_symbol
random.shuffle(new_list)
password = ""
for passes in new_list:
    password += passes


# random.shuffle(password)
print(f"Thank you for using our service!\nYour secured password is:\n {password}")

