class Fruit:
    FLAVOR = 'sweet'
    
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        print(f"This {self.name} is {self.FLAVOR}.")

class Citrus(Fruit):
    FLAVOR = 'tangy'

f_1 = Fruit('banana')
f_2 = Citrus('orange')

print(f_1.FLAVOR)
print(f_2.FLAVOR)

f_1.describe()
f_2.describe()
