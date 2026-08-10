class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

class Cow:

    def sound(self):
        print("Moo")


def make_sound(animal):
    animal.sound()

dog=Dog()
cat=Cat()
cow=Cow()

make_sound(dog)
make_sound(cat)
make_sound(cow)


# Polymorphism with inheritance

class Animal:

    def sound(self):
        print("Animal sound")


class DogAnimal(Animal):

    def sound(self):
        print("Bark")


class CatAnimal(Animal):

    def sound(self):
        print("Meow")


animals = [DogAnimal(), CatAnimal()]

for animal in animals:
    animal.sound()


# Built-in polymorphism

print(len("Kiran"))
print(len([10, 20, 30]))
print(len({"name": "Kiran", "age": 21}))

print(10 + 20)
print("10" + "20")
print([10] + [20])