from animals import Zebra, Giraffe, Tiger, Elephant, Snake
from animals import Cage

class Zoo:
    def __init__(self):
        self.cages = {}
    
    def add_cages(self, *new_cages: Cage):
        for cage in new_cages:
            self.cages[cage.id_num] = cage.caged_animals
    
    def __repr__(self):
        output = ''
        for cage_id, animals in self.cages.items():
            desc_animals = [f"{animal.color} {animal.species.lower()}" 
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
cage_1.add_animals(hulk, harry, rowena)

cage_2 = Cage(2)
cage_2.add_animals(sheila, blake, lucille)

city_zoo.add_cages(cage_1, cage_2)
print(city_zoo)
