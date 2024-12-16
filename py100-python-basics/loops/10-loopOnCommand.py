'''
Modify the following code so the loop continues iterating until the user inputs 'yes'.
'''

# original
# while True:
#     print('Should I stop looping?')
#     answer = input()

while True:
    print('Should I stop looping?')
    answer = input()
    if(answer == 'yes'):
        break

answer = 'no'
while answer != 'yes':
    print('Should I stop looping?')
    answer = input()