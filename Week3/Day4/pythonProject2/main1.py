from main import Dog
import random
class PetDog(Dog):
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age
        self.trained = False
    def train(self):
        self.trained = True
        print(self.bark())
    def play(*args):
        print(f"{*args} all play together")
    def do_a_trick(self):
        tricks = ['does a barrel roll',
'stands on his back legs',
'shakes your hand',
'plays dead']
        if self.trained == True:
            rtrick = random.choice(tricks)
            print(f"{self.name} {rtrick}")

class Family():
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = []
    def born(self, **kwargs):
            self.members.append(kwargs)
            print(
                f"Congratulations to the {self.last_name} family on the birth of {kwargs['name']}!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family {self.last_name}:")
        for member in self.members:
            print(member)

Smith = Family("Smith", [{'name':'Michael','age':35,'gender':'Male',
                     'is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}])
Smith.born('name'='George', 'age'=0, 'gender'='Male','is_child'=True})
Smith.family_presentation()
print(Smith.is_18('George'))


class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(
                        f"{member['incredible_name']} uses their power: {member['power']}!")
                else:
                    raise Exception(
                        f"{name} is not over 18 years old and cannot use their power.")
                return
        raise Exception(f"Member with name {name} not found.")

    def incredible_presentation(self):
        print("Here is our powerful family **")
        super().family_presentation()

incredibles_family = TheIncredibles('Incredibles')
incredibles_family.members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False,
     'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False,
     'power': 'read minds', 'incredible_name': 'SuperWoman'}
]
incredibles_family.incredible_presentation()

incredibles_family.born(name='Jack', age=0, gender='Male', is_child=True,
                        power='Unknown Power', incredible_name='BabyJack')

incredibles_family.incredible_presentation()
