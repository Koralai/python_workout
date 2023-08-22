class Sheep:
    def __init__(self, color):
        self.color = color
        self.species = 'sheep'
        self.number_of_legs = 4
        
    def __repr__(self):
        return f"A {self.color} {self.species} with {self.number_of_legs} legs"

class Wolf:
    def __init__(self, color):
        self.color = color
        self.species = 'wolf'
        self.number_of_legs = 4
        
    def __repr__(self):
        return f"A {self.color} {self.species} with {self.number_of_legs} legs"

class Snake:
    def __init__(self, color):
        self.color = color
        self.species = 'snake'
        self.number_of_legs = 0

    def __repr__(self):
        return f"A {self.color} {self.species} with {self.number_of_legs} legs"

class Parrot:
    def __init__(self, color):
        self.color = color
        self.species = 'parrot'
        self.number_of_legs = 2

    def __repr__(self):
        return f"A {self.color} {self.species} with {self.number_of_legs} legs"


henry = Sheep('black')
print(henry.color)
print(henry.species)
print(henry.number_of_legs)
print(henry)
