# Use Python's control structures to create a function that takes an ISO 639-1 language code and returns a greeting in that language. You can take the examples below or add whatever languages you like.

# function takes in a string thats an ISO 639-1 lanuage code
# check if the condition matches a case
# if it does, return a greeting in that language

def greet(lang_code):
  match lang_code:
    case 'en':
      return 'Hi'
    case 'fr':
      return 'Salut'
    case 'pt':
      return 'Ola'
    case 'de':
      return 'Hallo'
    case 'sv':
      return 'Hej'
    case 'af':
      return 'Haai'

# print(greet('en'))         # Hi!
# print(greet('fr'))         # Salut!
# print(greet('pt'))         # Olá!
# print(greet('de'))         # Hallo!
# print(greet('sv'))         # Hej!
# print(greet('af'))         # Haai!