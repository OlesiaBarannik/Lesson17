class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        pass

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print("meow")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print("woof woof")

Lapa = Cat("Lapa")
Barsik = Dog("Barsik")


def call(animals):
    for animal in animals:
        animal.talk()

call([Lapa, Barsik])