class Animal:
    def __init__(self, name, danger = False):
        self.name = name
        self.danger = danger

    def is_dangerous(animal):
        return animal.danger

class Human:
    pass

animal_1 = Animal('Кот')
animal_2 = Animal('Тигр', True)

print(Animal.is_dangerous(animal_1))
print(Animal.is_dangerous(animal_2))
