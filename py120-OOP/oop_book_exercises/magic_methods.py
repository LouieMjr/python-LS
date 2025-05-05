class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f'{self.color.capitalize()} {self.year} {self.model}'

    def __repr__(self):
        color = repr(self.color)
        year = repr(self.year)
        model = repr(self.model)
        return f'Car({model}, {year}, {color})'

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

import math

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    # __iadd__ method omitted; we don't need it for this exercise

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        new_x = self.x * other.x
        new_y = self.y * other.y
        return new_x + new_y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f'Vector({x}, {y})'

# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2)      # Vector(18, 8)
#
#
# print(v1 - v2) # Vector(-8, 16)
# print(v1 * v2) # 17
# print(abs(v1)) # 13.0



class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, vote):
        self.votes += vote
        return self



class Election(Candidate):

    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        tmp_max = 0
        max_votes = 0
        vote_count = 0
        winner = None

        for candidate in candidates:
            vote_count = candidate.votes
            if vote_count > tmp_max:
                tmp_max = vote_count
                winner = candidate.name

            max_votes += vote_count
            print(f'{candidate.name} : {vote_count} votes')

        print(f'\n{winner} won: {(tmp_max / max_votes)*100:.1f}% of votes')


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

print(mike_jones)

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()
