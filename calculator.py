
import art
import os

print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


keys = {"+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        }

quest = True


# while quest:
def start():
    first = float(input("What's the first number?:"))
    for value in keys:
        print(value)
    operation = input("Pick an operation:")
    second = int(input("What's the next number?:"))
    operated = keys[operation](n1=first, n2=second)
    return operated


# print(f" Your answer is {start()}")
capture = start()
print(capture)
# begin()


option = input(f"Type 'y' to continue calculating with {print(start())} , or type 'n' to start a new calculation:")
# if option == "y":


# else:
#     os.system("cls")
#     begin()
#interesting.
