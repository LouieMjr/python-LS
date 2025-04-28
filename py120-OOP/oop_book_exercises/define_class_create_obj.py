class Person:
    def __init__(self, name):
        self.name = name
        self.type = self.__class__.__name__
        #self.type = type(self).__name__
        print(f'Hi my name is {self.name} and i am a {self.type}')


george = Person('george')
print(george)

susan = Person('susan')
print(susan)
