class Subject:
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        return "RealSubject request"


class Proxy(Subject):
    def __init__(self):
        self._real_subject = RealSubject()

    def request(self):
        if self._check_access():
            return self._real_subject.request()
        else:
            return "Proxy request"

    def _check_access(self):
        return True


if __name__ == '__main__':
    proxy = Proxy()
    print(proxy.request())
