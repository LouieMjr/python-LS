from time import sleep
import json
from os import system

def open_json():
    with open('./messages.json', 'r') as file:
        return json.load(file)

MESSAGES = open_json()

def get_loan_amount(print_char):
    print_char(MESSAGES['ask_for_loan_amount'])
    try:
        loan_amount = int(input())
    except ValueError:
        system('clear')
        print_char(MESSAGES['invalid_input'])
        return get_loan_amount(print_char)
    system('clear')
    return loan_amount

def get_annual_percentage_rate(print_char):
    print_char(MESSAGES['ask_for_APR'])
    try:
        A_P_R = (float(input()) / 100)
    except ValueError:
        system('clear')
        print_char(MESSAGES['invalid_input'])
        return get_annual_percentage_rate(print_char)
    return A_P_R

def calculate_monthly_interest_rate(print_char):
    A_P_R = get_annual_percentage_rate(print_char)
    system('clear')
    monthly_interest_rate = (A_P_R / 12)
    return [monthly_interest_rate, A_P_R]

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

def print_char_msg_with_delay(message):
    for char in message:
        print(char, end='', flush=True)
        delay(0.02)

def calculate_monthly_payment(print_char):
    principle = get_loan_amount(print_char)
    monthly_rate, A_P_R = calculate_monthly_interest_rate(print_char)
    loan_term = convert_loan_term_to_months(print_char)

    monthly_payment = 0
    if monthly_rate == 0:
        monthly_payment = principle / loan_term
    else:
        monthly_payment = principle * (monthly_rate / (1 - (1 + monthly_rate) ** (-loan_term)))

    monthly_payment = f'{monthly_payment:.2f}'
    system('clear')
    display_loan_info([principle, A_P_R, monthly_rate, loan_term, monthly_payment])

def display_loan_info(loan_info_list):
    borrow_amount, annual_per, monthly_int, loan_duration, monthly_cost = loan_info_list

    borrow_amount_msg = f'{MESSAGES['borrow_amount']}{borrow_amount:,}.\n\n'
    annual_per_msg = f'{MESSAGES['APR']} {annual_per}%.\n'
    monthly_int_msg = f'{MESSAGES['monthly_interest_rate']} {monthly_int:.4f}%.\n'
    loan_term_msg = f'{MESSAGES['loan_duration']} {loan_duration} months.\n\n'
    monthly_payment_msg = f'{MESSAGES['monthly_payment']}{monthly_cost}\n'

    print_char_msg_with_delay(f'{borrow_amount_msg}{annual_per_msg}{monthly_int_msg}{loan_term_msg}')
    delay(0.8)
    print_char_msg_with_delay(f'{monthly_payment_msg}\n')

def restart_calc(print_char):
    print_char(MESSAGES['restart_calc'])
    response = input()
    match response[0].lower():
        case 'y':
            system('clear')
            start_loan_calc(print_char, None)
        case 'n':
            print_char(MESSAGES['goodbye'])
        case _:
            system('clear')
            print_char(MESSAGES['invalid_restart'])
            restart_calc(print_char)

def start_loan_calc(print_char, message = MESSAGES['welcome']):
    if message is not None:
        print_char(message)
        delay(0.8)
    calculate_monthly_payment(print_char)
    restart_calc(print_char)

start_loan_calc(print_char_msg_with_delay)