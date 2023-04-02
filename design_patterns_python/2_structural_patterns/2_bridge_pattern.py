class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return f"Abstraction: {self.implementation.operation_implementation()}"


class Implementation:
    def operation_implementation(self):
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA: Hello World"


class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB: Goodbye World"


if __name__ == '__main__':
    implementationA = ConcreteImplementationA()
    abstractionA = Abstraction(implementationA)
    print(abstractionA.operation())

    implementationB = ConcreteImplementationB()
    abstractionB = Abstraction(implementationB)
    print(abstractionB.operation())
