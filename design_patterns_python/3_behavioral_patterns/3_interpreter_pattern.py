class Context:
    def __init__(self, input_string):
        self._input_string = input_string
        self._index = 0

    def get_next_token(self):
        if self._index < len(self._input_string):
            token = self._input_string[self._index]
            self._index += 1
            return token
        return None


class Expression:
    def interpret(self, context):
        pass


class TerminalExpression(Expression):
    def __init__(self, data):
        self._data = data

    def interpret(self, context):
        if context.get_next_token() == self._data:
            return True
        return False


class NonterminalExpression(Expression):
    def __init__(self, expressions):
        self._expressions = expressions

    def interpret(self, context):
        for expression in self._expressions:
            if not expression.interpret(context):
                return False
        return True


if __name__ == '__main__':
    input_string = "ABAABBA"
    context = Context(input_string)

    expression1 = TerminalExpression("A")
    expression2 = TerminalExpression("B")
    expression3 = NonterminalExpression([expression1, expression2, expression1])

    result = expression3.interpret(context)
    print(f"{input_string} is {'' if result else 'not '}in the language")
