from animals import Zebra, Giraffe, Tiger, Elephant, Snake
from animals import Cage

class Zoo:
    def __init__(self):
        self.cages = {}
    
    def add_cages(self, *new_cages: Cage):
        for cage in new_cages:
            self.cages[cage.id_num] = cage.caged_animals
    
    def animals_by_color(self, color):
        output = []
        for animals in self.cages.values():
            for animal in animals:
                if animal.color == color.lower():
                    output.append(animal)
        return output
    
    def animals_by_legs(self, num_legs):
        output = []
        for animals in self.cages.values():
            for animal in animals:
                if animal.number_of_legs == num_legs:
                    output.append(animal)
        return output
    
    def total_legs_in_zoo(self):
        leg_count = 0
        for animals in self.cages.values():
            for animal in animals:
                leg_count += animal.number_of_legs
        return leg_count
    
    def __repr__(self):
        output = ''
        for cage_id, animals in self.cages.items():
            desc_animals = [f"{animal.color} {animal.species}" 
                            for animal in animals]
            output += f"Cage #{cage_id}: {', '.join(desc_animals)}\n"
        
        return output

harry = Zebra()
sophia = Zebra()
elaine = Giraffe()
hulk = Giraffe()
marcus = Elephant('brown')
rowena = Elephant('gray')
sheila = Tiger('white')
blake = Tiger('orange')
lucille = Snake('yellow')

city_zoo = Zoo()

cage_1 = Cage(1)
cage_1.add_animals(hulk, elaine, harry, rowena)

cage_2 = Cage(2)
cage_2.add_animals(sheila, blake, lucille)

city_zoo.add_cages(cage_1, cage_2)
print(city_zoo)

print(city_zoo.animals_by_color('yellow'))
print(city_zoo.animals_by_legs(4))
print(f"Number of legs of all animals in the zoo: {city_zoo.total_legs_in_zoo()}")
