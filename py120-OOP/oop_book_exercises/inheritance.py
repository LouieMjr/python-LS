# class Vehicle:
#
#     def __init__(self, wheels):
#         self._wheels = wheels
#         print(f'I have {self._wheels} wheels.')
#
#     def drive(self):
#         print('I am driving.')
#
# class Car(Vehicle):
#
#     def __init__(self):
#         print('Creating a car.')
#         super().__init__(4)
#
# class Truck(Vehicle):
#
#     def __init__(self):
#         print('Creating a truck.')
#         super().__init__(18)
#
# class Motorcycle(Vehicle):
#
#     def __init__(self):
#         print('Creating a motorcycle.')
#         super().__init__(2)
#
#     def drive(self):
#         super().drive()
#         print('No! I am riding!')
#
# car = Car()         # Creating a car.
#                     # I have 4 wheels
# car.drive()         # I am driving.
# print()
#
# truck = Truck()     # Creating a truck.
#                     # I have 18 wheels
# truck.drive()       # I am driving.
# print()
#
# motorcycle = Motorcycle() # Creating a motorcyle.
#                           # I have 2 wheels

# motorcycle.drive()  # I am driving.
#                     # No! I am riding!




class Vehicle:
    count = 0

    def __init__(self):
        Vehicle.count += 1

    @classmethod
    def vehicles(cls):
        return cls.count

class Car(Vehicle):
    def __init__(self):
        super().__init__()

class Truck(Vehicle):
    def __init__(self):
        super().__init__()

class Boat(Vehicle):
    def __init__(self):
        super().__init__()

print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8
