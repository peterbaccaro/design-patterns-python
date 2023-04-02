class Command:
    def execute(self):
        pass


class Receiver:
    def action(self):
        return "Receiver action"


class ConcreteCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        return self._receiver.action()


class Invoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        results = []
        for command in self._commands:
            results.append(command.execute())
        return results


if __name__ == '__main__':
    receiver = Receiver()
    command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.add_command(command)

    results = invoker.execute_commands()
    for result in results:
        print(result)
