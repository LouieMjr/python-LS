# Class based inheritance works great when it's used to model hierarchical domains. Let's take a look at a few practice problems. Suppose we're building a software system for a pet hotel business, so our classes deal with pets.
#
# Given this class:

class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())      # sleeping!

# One problem is that we need to keep track of different breeds of dogs, since they have slightly different behaviors. For example, bulldogs snore when they sleep, but other dogs do not. Okay, I have no idea if that's entirely true; I suspect it isn't. Let's pretend it is.
#
# Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"

class Bulldog(Dog):
    def sleep(self):
        return 'Snoring!'

tino = Bulldog()
print(tino.speak())
print(tino.sleep())


# Let's create a few more methods for our Dog class.

# Create a new class called Cat, which can do everything a dog can, except fetch. Assume the methods do the exact same thing. Hint: don't copy and paste any methods from Dog into Cat; come up with a class hierarchy instead.

class Pet:
    def speak():
        pass

    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

    # def speak(self):
    #     return 'bark!'
    #
    # def sleep(self):
    #     return 'sleeping!'
    #
    # def run(self):
    #     return 'running!'
    #
    # def jump(self):
    #     return 'jumping!'


class Bulldog(Dog):
    def sleep(self):
        return "snoring!"

class Cat(Pet):
    def speak(self):
        return 'meow!'

print('______________')
beanie = Dog()
print(beanie.fetch())
print(beanie.speak())

pumpkin = Bulldog()
print(pumpkin.sleep()) # snoring
print(pumpkin.run()) 

snowflake = Cat()
print(snowflake.jump())
print(snowflake.speak())

try:
    snowflake.fetch()
except Exception as exception:
    print(exception.__class__.__name__, exception, "\n")
    # AttributeError 'Cat' object has no attribute 'fetch'

print(Bulldog.mro())
print([cls.__name__ for cls in Bulldog.mro()])
