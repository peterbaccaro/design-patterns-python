from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class Leaf(Component):
    def operation(self):
        return "Leaf operation"


class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Composite operation with {', '.join(results)}"


if __name__ == '__main__':
    leaf1 = Leaf()
    leaf2 = Leaf()
    composite = Composite()
    composite.add(leaf1)
    composite.add(leaf2)

    composite2 = Composite()
    composite2.add(composite)
    composite2.add(Leaf())

    print(composite2.operation())
