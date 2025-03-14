class A:
    def speak(self):
        print("I am an animal")
class B:
    def has_fur(self):
        print("I have fur")
class Dog(A,B):
    def bark(self):
        print("I bark")
dog = Dog()
dog.speak()
dog.has_fur() 
dog.bark() 
