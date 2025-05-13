# Change the following code so that creating a new Truck automatically calls start_engine.


class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def __init__(self, year):
        super().__init__(year)
        self.start_engine()

    def start_engine(self):
        print('Ready to go!')

class Car(Vehicle):
    def __init__(self, year):
        super().__init__(year)

# Comments show expected output
truck1 = Truck(1994)          # Ready to go!
print(truck1.year)            # 1994

car1 = Car(2000)
print(car1.year)

print(Vehicle.year)
