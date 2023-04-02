class AbstractClass:
    def template_method(self):
        self._operation1()
        self._operation2()
        self._operation3()

    def _operation1(self):
        print("AbstractClass: _operation1")

    def _operation2(self):
        pass

    def _operation3(self):
        print("AbstractClass: _operation3")


class ConcreteClass1(AbstractClass):
    def _operation2(self):
        print("ConcreteClass1: _operation2")


class ConcreteClass2(AbstractClass):
    def _operation2(self):
        print("ConcreteClass2: _operation2")

    def _operation3(self):
        print("ConcreteClass2: _operation3")


if __name__ == '__main__':
    concrete_class_1 = ConcreteClass1()
    concrete_class_1.template_method()

    concrete_class_2 = ConcreteClass2()
    concrete_class_2.template_method()
