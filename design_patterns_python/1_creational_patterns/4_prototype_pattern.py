import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Person(Prototype):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"


if __name__ == '__main__':
    person1 = Person("John", 30)
    person2 = person1.clone()
    person2.name = "Jane"
    person2.age = 25

    print(person1)
    print(person2)
