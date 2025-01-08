# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.

from random import randrange, randint

def how_old():
    name = input('Whats the persons name? ').capitalize()
    name = 'Teddy' if name == '' else name
    age = randint(20, 100)
    return f'{name} is {age} years old'

print(how_old())