# Using the code snippet provided below, add a setter method named name. Then, rename kitty to 'Luna' and invoke greet again.

class Cat:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet()
kitty.name = 'Luna'
kitty.greet()
