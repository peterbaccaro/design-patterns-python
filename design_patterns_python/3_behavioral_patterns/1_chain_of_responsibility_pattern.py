class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        pass


class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == "Request1":
            return "ConcreteHandler1 handled the request"
        elif self._successor:
            return self._successor.handle_request(request)
        else:
            return "No handler found"


class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == "Request2":
            return "ConcreteHandler2 handled the request"
        elif self._successor:
            return self._successor.handle_request(request)
        else:
            return "No handler found"


if __name__ == '__main__':
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2(handler1)

    print(handler2.handle_request("Request1"))
    print(handler2.handle_request("Request2"))
    print(handler2.handle_request("Request3"))
