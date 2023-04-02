class Mediator:
    def send(self, message, sender):
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        self._colleague1 = Colleague1(self)
        self._colleague2 = Colleague2(self)

    def send(self, message, sender):
        if sender == self._colleague1:
            self._colleague2.receive(message)
        else:
            self._colleague1.receive(message)


class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator


class Colleague1(Colleague):
    def send(self, message):
        self._mediator.send(message, self)

    def receive(self, message):
        print(f"Colleague1 received message: {message}")


class Colleague2(Colleague):
    def send(self, message):
        self._mediator.send(message, self)

    def receive(self, message):
        print(f"Colleague2 received message: {message}")


if __name__ == '__main__':
    mediator = ConcreteMediator()
    colleague1 = Colleague1(mediator)
    colleague2 = Colleague2(mediator)

    colleague1.send("Hello from Colleague1")
    colleague2.send("Hello from Colleague2")
