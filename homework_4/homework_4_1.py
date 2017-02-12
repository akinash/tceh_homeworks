class Person:
    __known = []

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def know(self, person):
        self.__known.append(person)

    def is_known(self, person):
        return person in self.__known

person_1 = Person(15, 'Артем')
person_2 = Person(24, 'Дима')
person_3 = Person(35, 'Антон')

person_1.know(person_2)

print(person_1.is_known(person_2))
