# winning scenarios

# rock:
# rock > scissor

# paper:
# paper > rock

# scissors:
# scissors > paper
from time import sleep

def delay(time):
    sleep(time)

def print_with_typing_effect(message):
    for char in message:
        print(char, end='', flush=True)
        delay(0.02)

def get_user_choice():
    print_with_typing_effect('Make your selection: Rock(r), Paper(p), Scissors(s): ')
    user_choice = input().upper()

    # validate input
    choices = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }

    if user_choice[0] in choices:
        user_choice = choices[user_choice[0]]
        print_with_typing_effect('You picked: ' + user_choice + '\n')
    # validate input could be put in separate function

get_user_choice()