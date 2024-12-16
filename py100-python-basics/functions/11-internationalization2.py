# Building on your solutions from the previous exercises, write a function local_greet that takes a locale as input, and returns a greeting. The locale lets us greet people from different countries appropriately, even when they share a common language, for example:

from localeP1 import extract_language
from localeP2 import extract_region
from internationalization1 import greet


def local_greet(locale):
  region = extract_region(locale)
  language = extract_language(locale)
  match (language, region):
    case ('en', 'US'):
        return 'Hey!'
    case ('en', 'GB'):
        return 'Hello!'
    case ('en', 'AU'):
        return 'Howdy!'
    case _:
        return greet(language)
  
print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

# Distinguish greetings for English speaking countries like the US, UK, Canada, or Australia in your implementation, and feel free to fall back on the language-specific greetings in all other cases, for example:

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!
print(local_greet('pt_MA.UTF-8'))       # Ola!