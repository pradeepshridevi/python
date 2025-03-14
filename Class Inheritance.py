class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed

    def speak(self):
        return "Woof! Woof!"

    def show_breed(self):
        return f"I am a {self.breed}."
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")
print(f"{animal.name} says: {animal.speak()}")
print(f"{dog.name} says: {dog.speak()}")
print(dog.show_breed())
