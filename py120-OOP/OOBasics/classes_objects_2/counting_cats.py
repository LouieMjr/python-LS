# Create a class named Cat that tracks the number of times a new Cat object is instantiated. The total number of Cat instances should be printed when total is invoked.

class Cat:
    counter = 0
    def __init__(self):
        Cat.counter += 1

    @classmethod
    def total(cls):
        print(cls.counter)



Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3
