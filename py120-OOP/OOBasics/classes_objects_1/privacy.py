# Using the code snippet provided below, modify the instance variable name to indicate to developers that it is intended for internal use only.

class Cat:
    def __init__(self, name):
        self._name = name 
        # or __name; will mangle and add a prefix of _ClassName to it to avoid name clashes with attributes defined by subclasses

    def greet(self):
        print(f"Hello! My name is {self._name}!")

kitty = Cat('Sophie')
kitty.greet()
