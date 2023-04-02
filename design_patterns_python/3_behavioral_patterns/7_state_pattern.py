class State:
    def do_action(self, context):
        pass


class StartState(State):
    def do_action(self, context):
        print("Player is in start state")
        context.set_state(self)


class StopState(State):
    def do_action(self, context):
        print("Player is in stop state")
        context.set_state(self)


class Context:
    def __init__(self):
        self._state = None

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def do_action(self):
        self._state.do_action(self)


if __name__ == '__main__':
    context = Context()

    start_state = StartState()
    start_state.do_action(context)
    print(f"Current state: {type(context.get_state()).__name__}")

    stop_state = StopState()
    stop_state.do_action(context)
    print(f"Current state: {type(context.get_state()).__name__}")
