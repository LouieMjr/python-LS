class Person:
    def __init__(self, name):
        self.name = name
        self.type = self.__class__.__name__
        #self.type = type(self).__name__
        print(f'Hi my name is {self.name} and i am a {self.type}')


# george = Person('george')
# print(george)

# susan = Person('susan')
# print(susan)

class Foo1:

    @classmethod
    def bar(cls):
        print('this is bar in Foo1')

    def qux(self):
        print(self)
        type(self).bar()
        self.__class__.bar()
        self.bar()
        Foo1.bar()

class Foo2(Foo1):

    @classmethod
    def bar(cls):
        print('this is bar in Foo2')

foo1 = Foo1()
foo1.qux()
# this is bar in Foo1
# this is bar in Foo1
# this is bar in Foo1
# this is bar in Foo1

foo2 = Foo2()
foo2.qux()
# this is bar in Foo2
# this is bar in Foo2
# this is bar in Foo2
# this is bar in Foo1
