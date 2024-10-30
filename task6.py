class Animal:
    def sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Barks")

class Cat(Animal):
    def sound(self):
        print("Meow")

def make_animal_sound(Animal):
    return Animal.sound()

dog = Dog()
cat = Cat()

make_animal_sound(dog)
make_animal_sound(cat)

    
