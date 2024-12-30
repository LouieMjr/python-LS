from time import sleep
import json
import os

def open_json():
    with open('./messages.json', 'r') as file:
        return json.load(file)

MESSAGES = open_json()

def get_loan_amount_from_user():
    print_char_horizontally(MESSAGES['ask_for_loan_amount'])
    loan_amount = float(input())
    return loan_amount

def get_annual_percentage_rate():
    print_char_horizontally(MESSAGES['ask_for_APR'])
    APR = float(input())
    return APR

# def get_loan_duration():
    

def delay(time):
    sleep(time)

def print_char_horizontally(message):
    for char in message:
        print(char, end='', flush=True)
        delay(0.03)

def start_loan_calc():
    print_char_horizontally(MESSAGES['welcome'])
    delay(1.5)
    loan_amount = get_loan_amount_from_user()
    print(get_annual_percentage_rate())

start_loan_calc()