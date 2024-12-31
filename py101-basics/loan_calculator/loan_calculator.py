from time import sleep
import json
from os import system

def open_json():
    with open('./messages.json', 'r') as file:
        return json.load(file)

MESSAGES = open_json()

def get_loan_amount_from_user(print_char):
    print_char(MESSAGES['ask_for_loan_amount'])
    try:
        loan_amount = int(input())
    except ValueError:
        system('clear')
        print_char(MESSAGES['invalid_input'])
        return get_loan_amount_from_user(print_char)
    system('clear')
    return loan_amount

def get_annual_percentage_rate(print_char):
    print_char(MESSAGES['ask_for_APR'])
    try:
        APR = (float(input()) / 100)
    except ValueError:
        system('clear')
        print_char(MESSAGES['invalid_input'])
        return get_annual_percentage_rate(print_char)
    return APR

def calculate_monthly_interest_rate(print_char):
    APR = get_annual_percentage_rate(print_char)
    system('clear')
    monthly_interest_rate = (APR / 12)
    return [monthly_interest_rate, APR]

def get_loan_duration_years(print_char):
    print_char(MESSAGES['ask_for_loan_duration'])
    try:
        loan_term = int(input())
    except ValueError:
        system('clear')
        print_char(MESSAGES['invalid_input'])
        return get_loan_duration_years(print_char)
    return loan_term

def convert_loan_term_to_months(print_char):
    loan_term_years = get_loan_duration_years(print_char)
    months_in_one_year = 12
    loan_duration_in_months = months_in_one_year * loan_term_years
    return loan_duration_in_months

def delay(time):
    sleep(time)

def print_char_horizontally(message):
    for char in message:
        print(char, end='', flush=True)
        delay(0.02)

def calculate_monthly_payment(print_char):
    principle = get_loan_amount_from_user(print_char)
    monthly_rate, APR = calculate_monthly_interest_rate(print_char)
    loan_term = convert_loan_term_to_months(print_char)

    monthly_payment = principle * (monthly_rate / (1 - (1 + monthly_rate) ** (-loan_term)))
    monthly_payment = f'{monthly_payment:.2f}'

    borrow_amount_msg = f'{MESSAGES['borrow_amount']}{principle:,}.\n\n'
    annual_per_rate = f'{MESSAGES['APR']} {APR}%.\n'
    monthly_int_rate = f'{MESSAGES['monthly_interest_rate']} {monthly_rate:.5f}%.\n'
    loan_duration = f'{MESSAGES['loan_duration']} {loan_term} months.\n\n'
    monthly_payment_msg = f'{MESSAGES['monthly_payment']}{monthly_payment}'

    system('clear')

    print_char(f'{borrow_amount_msg}{annual_per_rate}{monthly_int_rate}{loan_duration}')
    delay(0.8)
    print_char(f'{monthly_payment_msg}\n')

def start_loan_calc():
    print_char_horizontally(MESSAGES['welcome'])
    delay(0.8)
    calculate_monthly_payment(print_char_horizontally)

start_loan_calc()