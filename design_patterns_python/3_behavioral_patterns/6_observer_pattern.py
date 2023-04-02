class Observer:
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received message: {message}")


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


if __name__ == '__main__':
    subject = Subject()

    observer1 = Observer("Observer1")
    observer2 = Observer("Observer2")
    observer3 = Observer("Observer3")

    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)

    subject.notify("Hello World!")

    subject.detach(observer2)

    subject.notify("Goodbye World!")
