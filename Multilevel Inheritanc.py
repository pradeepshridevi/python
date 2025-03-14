class Animal:
    def breathe(self):
        return "Breathing..."

class Mammal(Animal):
    def feed_milk(self):
        return "Feeding milk to young ones."
class Dog(Mammal):
    def bark(self):
        return "Woof! Woof!"

dog = Dog()

print(dog.breathe())  
print(dog.feed_milk()) 
print(dog.bark())
