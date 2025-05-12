# Create a class named Cat for which calling Cat.generic_greeting prints Hello! I'm a cat!.

class Cat:
    @classmethod
    def generic_greeting(cls):
        print(f'Hello Im a {cls.__name__}!')

# Cat.generic_greeting()
kitty = Cat()
print(type(kitty))
print(type(kitty).generic_greeting())
