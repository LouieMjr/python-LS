# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.type = self.__class__.__name__
#         #self.type = type(self).__name__
#         print(f'Hi my name is {self.name} and i am a {self.type}')


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

        # constructor
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self.speed = 0

        # instance method
    def start_engine(self):
        print(f'{self._model}s engine is on')

        # instance method
    def brake(self, number):
        self.speed -= number
        print(f'{self._model}s brake is applied')
        print(f'You decelerated {number} mph')

        # instance method
    def stop_engine(self):
        self.speed = 0
        print(f'{self._model}s engine is off')

        # instance method
    def speed_up(self, number):
        self.speed += number
        print(f'You accelerated {number} mph')

        # instance method
    def get_speed(self):
        print(f"You're going {self.speed} mph")

    # instance method
    @property
    def color(self):
        return self._color

    # instance method
    @color.setter
    def color(self, new_color):
        self._color = new_color

    # instance method
    @property
    def model(self):
        return self._model

    # instance method
    @property
    def year(self):
        return self._year

    @classmethod
    def gas_mileage(cls, gallons, miles):
        mileage = miles / gallons
        print(f'{mileage:.02f} miles per gallon')

    # instance method
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

print(Car.gas_mileage(24, 280))

print(model_3.year)
print(model_3.model)

print(model_3.color)
model_3.color = 'Space gray'
print(model_3.color)

model_3.spray_paint_car('black')
print(model_3.color)

# model_3.year = 2025 # has no setter AttributError


class Person:

    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)

    @property
    def name(self):
        return f'{self._first_name.capitalize()} {self._last_name.capitalize()}'

    @name.setter
    def name(self, name_tuple):
        self._set_name(name_tuple[0], name_tuple[1])

    @classmethod
    def _validate(cls, *names):
        for name in names:
            if not name.isalpha():
                raise ValueError('Name must be alphabetic only.')

    def _set_name(self, first_name, last_name):
        Person._validate(first_name, last_name)
        self._first_name = first_name
        self._last_name = last_name



print('_________------------________')
actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.
friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
# friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.
