class Strategy:
    def do_operation(self, num1, num2):
        pass


class OperationAdd(Strategy):
    def do_operation(self, num1, num2):
        return num1 + num2


class OperationSubtract(Strategy):
    def do_operation(self, num1, num2):
        return num1 - num2


class OperationMultiply(Strategy):
    def do_operation(self, num1, num2):
        return num1 * num2


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, num1, num2):
        return self._strategy.do_operation(num1, num2)


if __name__ == '__main__':
    context = Context(OperationAdd())
    print(f"10 + 5 = {context.execute_strategy(10, 5)}")

    context = Context(OperationSubtract())
    print(f"10 - 5 = {context.execute_strategy(10, 5)}")

    context = Context(OperationMultiply())
    print(f"10 * 5 = {context.execute_strategy(10, 5)}")
