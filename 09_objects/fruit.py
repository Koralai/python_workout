class Fruit:
    FLAVOR = 'sweet'

class Citrus(Fruit):
    FLAVOR = 'tangy'

apple = Fruit()
orange = Citrus()

print(apple.FLAVOR)
print(orange.FLAVOR)
