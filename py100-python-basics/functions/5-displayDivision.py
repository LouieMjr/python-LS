# Without running the following code, determine what it will print:

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three
# will print nothing since function hasnt been invoked/called