
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def attack(self, victim):
        return f"{victim} has been bitten"

a = Bengal("Simba", 3)
b = Siamese("Nala", 2)
c = Chartreux("Milo", 1)
all_cats = [a, b, c]
sara_pets = Pets(all_cats)
sara_pets.walk()

#exercise 2
class Dog():
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def bark(self):
        print("{} is barking".format(self.name))

    def run_speed(self):
        return ((self.weight/self.age)*10)

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            return f"{self.name} won"
        else:
            return f"{other_dog.name} won"

Rex = Dog("Rex", 10,10)
Toby = Dog("Toby", 5,5)
Clifford = Dog("Clifford", 100, 2)

print(Dog.fight(Toby, Clifford))


