class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        return f"Flyweight operation with shared state '{self._shared_state}' and unique state '{unique_state}'"


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]


if __name__ == '__main__':
    factory = FlyweightFactory()
    flyweight1 = factory.get_flyweight("shared_state")
    flyweight2 = factory.get_flyweight("shared_state")
    flyweight3 = factory.get_flyweight("other_shared_state")

    print(flyweight1.operation("unique_state1"))
    print(flyweight2.operation("unique_state2"))
    print(flyweight3.operation("unique_state3"))
