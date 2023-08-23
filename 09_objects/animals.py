class Animal:
    def __init__(self, color, number_of_legs, sound, food_chain_type):
        self.color = color
        self.species = self.__class__.__name__
        self.number_of_legs = number_of_legs
        self.sound = sound
        self.food_chain_type = food_chain_type
        
    def __repr__(self):
        return (f'"{self.sound.capitalize()}!" says the {self.color} '
                f"{self.species.lower()} with {self.number_of_legs} legs.")

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=4, sound='baa', 
                         food_chain_type='herbivore')

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=4, sound='awooo',
                         food_chain_type='carnivore')

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=0, sound='ssss',
                         food_chain_type='carnivore')

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, number_of_legs=2, sound='squawk',
                         food_chain_type='omnivore')

class Cage:
    def __init__(self, id_num):
        self.id_num = id_num
        self.caged_animals = []
    
    def add_animals(self, *animals: Animal):
        for animal in animals:
            if len(self.caged_animals) == 0:
                self.caged_animals.append(animal)
            else:
                current_animal_types = [animal.food_chain_type 
                                        for animal in self.caged_animals]

                if animal.food_chain_type in current_animal_types:
                    self.caged_animals.append(animal)
                else:
                    print(f"Oops! You shouldn't put {animal.food_chain_type}s "
                          f"in the same cage with {''.join(current_animal_types)}s.")
    
    def set_free_animals(self, *animals: Animal):
        for animal in animals:
            self.caged_animals.remove(animal)
    
    def __repr__(self):
        animal_descriptions = [f"{animal.color} {animal.species.lower()}" 
                               for animal in self.caged_animals]
        
        return f"Animals in cage #{self.id_num}: {', '.join(animal_descriptions)}"

henry = Sheep('black')
print(henry)
daisy = Parrot('green')
print(daisy.number_of_legs)
print(daisy)
sirius = Wolf('black')
print(sirius)

c1 = Cage(1)
c1.add_animals(henry, daisy, sirius, henry)
print(c1)
c1.set_free_animals(henry)
print(c1)
