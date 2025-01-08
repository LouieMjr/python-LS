# Build a program that displays when the user will retire and how many years she has to work till retirement.

from datetime import datetime

def retire():
    current_age = int(input('What is your age? '))
    retirement_age = int(input('What age would you like to retire? '))

    current_year = datetime.now().year
    years_left = retirement_age - current_age
    retirement_year = current_year + years_left
    
    return (f"\nIts {current_year}. You will retire in {retirement_year}.\n"
            f'You have only {years_left} years of work to go!')

print(retire())