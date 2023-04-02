class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    def create_animal(self, name):
        if name == "dog":
            return Dog(name)
        elif name == "cat":
            return Cat(name)
        else:
            return None


if __name__ == '__main__':
    dog = AnimalFactory().create_animal("dog")
    print(isinstance(dog, Dog))  # Output: True
