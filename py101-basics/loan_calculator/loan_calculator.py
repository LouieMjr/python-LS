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

def calculate_monthly_interest_rate():
    APR = get_annual_percentage_rate()
    monthly_interest_rate = APR / 12
    return monthly_interest_rate

def get_loan_duration_years():
    print_char_horizontally(MESSAGES['ask_for_loan_duration'])
    loan_term = int(input())
    return loan_term

def convert_loan_term_to_months():
    loan_term_years = get_loan_duration_years()
    months_in_one_year = 12
    loan_duration_in_months = months_in_one_year * loan_term_years
    return loan_duration_in_months

def delay(time):
    sleep(time)

def print_char_horizontally(message):
    for char in message:
        print(char, end='', flush=True)
        delay(0.03)

def calculate_monthly_payment():
    loan_amount = get_loan_amount_from_user()
    monthly_interest_rate = calculate_monthly_interest_rate()
    loan_term_months = convert_loan_term_to_months()

def start_loan_calc():
    print_char_horizontally(MESSAGES['welcome'])
    delay(1.5)
    calculate_monthly_payment()

start_loan_calc()