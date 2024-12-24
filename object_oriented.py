class Dog:
    species = 'Canine'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        print(f"Dog name is {self.name}")

class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")

class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name}Guides the way!")

dog1 = Dog('Buddy', 3)
print(dog1.name, dog1.age)