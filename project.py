class Animal:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def make_sound(self):
        print("Some generic sound")

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

class Dog(Animal):
    def make_sound(self):
        print("Gaf Gaf")

class Cat(Animal):
    def make_sound(self):
        print("Meow Meow")

class Cow(Animal):
    def make_sound(self,):
        print("Moo MOo")

animals = [Dog("Rex", 5), Cat("Murka", 3), Cow("Manya", 2)]

for animal in animals:
   print(f"Animal: {animal}, Name: {animal.name}, Age: {animal.get_age()},")
   animal.make_sound()
