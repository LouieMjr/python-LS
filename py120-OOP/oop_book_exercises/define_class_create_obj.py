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

# foo1 = Foo1()
# foo1.qux()
# this is bar in Foo1
# this is bar in Foo1
# this is bar in Foo1
# this is bar in Foo1

# foo2 = Foo2()
# foo2.qux()
# this is bar in Foo2
# this is bar in Foo2
# this is bar in Foo2
# this is bar in Foo1



class Animal:

    @classmethod
    def make_sound(cls):
        print(cls)
        print(f'{cls.__name__}: A generic sound')

class Dog(Animal):

    @classmethod
    def make_sound(cls):
        super().make_sound()
        print(f'{cls.__name__}: Bark')

# Dog.make_sound()
# dog = Animal()
# dog.make_sound()
# Dog: A generic sound
# Dog: Bark


class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self.speed = 0

    def start_engine(self):
        print(f'{self._model}s engine is on')

    def brake(self, number):
        self.speed -= number
        print(f'{self._model}s brake is applied')
        print(f'You decelerated {number} mph')

    def stop_engine(self):
        self.speed = 0
        print(f'{self._model}s engine is off')

    def speed_up(self, number):
        self.speed += number
        print(f'You accelerated {number} mph')

    def get_speed(self):
        print(f"You're going {self.speed} mph")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    def spray_paint_car(self, color):
        self._color = color
        print(f'Great paint job, loving the {color}')
        




model_3 = Car('Tesla Model 3', 2020, 'white')
print(model_3.start_engine())
print(model_3.get_speed())
print(model_3.speed_up(10))
print(model_3.get_speed())
print(model_3.speed_up(40))
print(model_3.get_speed())
print(model_3.brake(20))
print(model_3.get_speed())
print(model_3.brake(20))
print(model_3.stop_engine())


print(model_3.year)
print(model_3.model)

print(model_3.color)
model_3.color = 'Space gray'
print(model_3.color)

model_3.spray_paint_car('black')
print(model_3.color)

# model_3.year = 2025 # has no setter AttributError



















