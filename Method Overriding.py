class Animal:
    def speak(self):
        return "Some generic animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self): 
        return "Meow! Meow!"

dog = Dog()
cat = Cat()
generic_animal = Animal()

print("Dog says:", dog.speak())  
print("Cat says:", cat.speak())  
print("Generic Animal says:", generic_animal.speak())
