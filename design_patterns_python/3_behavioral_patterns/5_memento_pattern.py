class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    def __init__(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def set_memento(self, memento):
        self._state = memento.get_state()

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        print(f"State set to: {self._state}")


class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


if __name__ == '__main__':
    originator = Originator("State1")
    print(f"Current state: {originator.get_state()}")

    caretaker = Caretaker()
    caretaker.add_memento(originator.create_memento())

    originator.set_state("State2")
    print(f"Current state: {originator.get_state()}")

    caretaker.add_memento(originator.create_memento())

    originator.set_state("State3")
    print(f"Current state: {originator.get_state()}")

    originator.set_memento(caretaker.get_memento(0))
    print(f"Current state after restoring from Memento 0: {originator.get_state()}")

    originator.set_memento(caretaker.get_memento(1))
    print(f"Current state after restoring from Memento 1: {originator.get_state()}")
