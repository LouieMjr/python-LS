'''
Initialize a variable weather with a string value being 'sunny', 'rainy', or whatever weather condition you choose. Then, write an if statement that prints:

It's a beautiful day! if weather's value is 'sunny'
Grab your umbrella. if weather's value is 'rainy'
Let's stay inside. if weather's value is anything else


Test your code with different values for weather.
'''

conditions = 'sunny'
# if conditions == 'sunny':
#   print("It's a beautiful day!")
# elif conditions == 'rainy':
#   print("Grab your umbrella!")
# else:
#   print("Lets stay inside!")


match conditions:
    case 'sunny':
      print("It's a beautiful day!")
    case 'rainy':
      print("Grab your umbrella!")
    case _: # default case
      print("Lets stay inside!")