# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

def tip_calc():
    bill = float(input('What is the bill? '))
    tip_percentage = float(input('what is the tip percentage? '))

    real_tip_perc = tip_percentage / 100
    
    print(f'The tip is ${bill * real_tip_perc:.2f} and the total with the tip added is ${(bill * real_tip_perc) + bill:.2f}')

tip_calc()