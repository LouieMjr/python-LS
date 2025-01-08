# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).


def greet():
    name = input('What is your name? ')
    greeting = None
    if name.endswith('!'):
        greeting = f'Hello {name} why are we yelling?'.upper()
    else:
        greeting = f'Hello {name}'

    return greeting

print(greet())
# What is your name? Sue
# Hello Sue.

# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?