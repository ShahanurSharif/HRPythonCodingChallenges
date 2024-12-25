class Dog:
    def sound(self):
        print("dog sound")

class Labrador:
    def sound(self):
        print("labrador sound")

class Beagle(Dog):
    def sound(self):
        print("Beagle Barks")


class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
    print(dog.sound())

calc = Calculator()
# print(calc.add(5, 10))
# print(calc.add(5, 10, 15))