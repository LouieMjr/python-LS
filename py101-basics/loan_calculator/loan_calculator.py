from time import sleep
import json
import os

def open_json():
    with open('./messages.json', 'r') as file:
        return json.load(file)

MESSAGES = open_json()

def get_loan_amount_from_user():
    print_char_one_by_one(MESSAGES['ask_for_loan_amount'])
    loan_amount = input()
    return loan_amount

def delay(time):
    sleep(time)

def print_char_one_by_one(message):
    for char in message:
        print(char, end='', flush=True)
        delay(0.03)

    # print('\n')

def start_loan_calc():
    print_char_one_by_one(MESSAGES['welcome'])
    delay(2)
    print(get_loan_amount_from_user())

start_loan_calc()