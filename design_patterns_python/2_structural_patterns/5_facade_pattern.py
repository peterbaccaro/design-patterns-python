class SubsystemA:
    def operation1(self):
        return "Subsystem A, Operation 1"

    def operation2(self):
        return "Subsystem A, Operation 2"


class SubsystemB:
    def operation1(self):
        return "Subsystem B, Operation 1"

    def operation2(self):
        return "Subsystem B, Operation 2"


class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self):
        results = []
        results.append(self._subsystem_a.operation1())
        results.append(self._subsystem_a.operation2())
        results.append(self._subsystem_b.operation1())
        results.append(self._subsystem_b.operation2())
        return f"Facade operation with {', '.join(results)}"


if __name__ == '__main__':
    facade = Facade()
    print(facade.operation())
