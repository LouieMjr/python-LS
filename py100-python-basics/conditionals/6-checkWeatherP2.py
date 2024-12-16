'''
Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement. Feel free to add more cases besides 'sunny' and 'rainy'.
'''

conditions = 'sunny'

match conditions:
    case 'sunny':
      print("It's a beautiful day!")
    case 'rainy':
      print("Grab your umbrella!")
    case _: # default case
      print("Lets stay inside!")