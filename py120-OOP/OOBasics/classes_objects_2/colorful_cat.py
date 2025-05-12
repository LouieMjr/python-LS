# Create a class named Cat that prints a greeting when the greet instance method is invoked. The greeting should include the name and color of the cat. Use a class constant to define the color.

class Cat:
    MY_COLOR = 'purple'
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def greet(self):
        print(f'Hello! My name is {self.name} and Im a {Cat.MY_COLOR} cat!')


kitty = Cat('Sophie')
kitty.greet()
# Hello! My name is Sophie and I'm a purple cat!
