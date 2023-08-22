class Animal:
    def __init__(self, color, number_of_legs):
        self.color = color
        self.species = self.__class__.__name__
        self.number_of_legs = number_of_legs
        
    def __repr__(self):
        return f"A {self.color} {self.species.lower()} with {self.number_of_legs} legs"

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=4)

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=2)


henry = Sheep('black')
print(henry)
daisy = Parrot('green')
print(daisy.number_of_legs)
print(daisy)
