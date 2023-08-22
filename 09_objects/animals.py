class Animal:
    def __init__(self, color, number_of_legs, sound):
        self.color = color
        self.species = self.__class__.__name__
        self.number_of_legs = number_of_legs
        self.sound = sound
        
    def __repr__(self):
        return (f'"{self.sound.capitalize()}!" says the {self.color} '
                f"{self.species.lower()} with {self.number_of_legs} legs.")

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=4, sound='baa')

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=4, sound='awooo')

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=0, sound='ssss')

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=2, sound='squawk')


henry = Sheep('black')
print(henry)
daisy = Parrot('green')
print(daisy.number_of_legs)
print(daisy)
sirius = Wolf('black')
print(sirius)
