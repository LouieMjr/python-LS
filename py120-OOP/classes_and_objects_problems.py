# Given the following code, create the Person class needed to make the code work as shown:

# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#
# bob = Person('bob')
# print(bob.name)           # bob
# bob.name = 'Robert'
# print(bob.name)           # Robert


# Modify the class definition from above to facilitate the following methods. Note that there is no name= setter method now.

class Person:
    def __init__(self, name):
        parts = name.split()
        self.first_name = parts[0]
        self.last_name = ''
        if len(parts) > 1:
            self.last_name = parts[1]

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        print(f'Setter called with: {first_name}')
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name


bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith
bob.first_name = 'Rob'
print(bob.name)             # Rob Smith



