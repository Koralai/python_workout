class Animal:
    def __init__(self, color, species='', number_of_legs=0):
        self.color = color
        self.species = species
        self.number_of_legs = number_of_legs
        
    def __repr__(self):
        return f"A {self.color} {self.species} with {self.number_of_legs} legs"

class Sheep(Animal):
    def __init__(self, color, species='sheep', number_of_legs=4):
        super().__init__(color, species, number_of_legs)

class Wolf(Animal):
    def __init__(self, color, species='wolf', number_of_legs=4):
        super().__init__(color, species, number_of_legs)

class Snake(Animal):
    def __init__(self, color, species='snake', number_of_legs=0):
        super().__init__(color, species, number_of_legs)

class Parrot(Animal):
    def __init__(self, color, species='parrot', number_of_legs=2):
        super().__init__(color, species, number_of_legs)


henry = Sheep('black')
print(henry)
