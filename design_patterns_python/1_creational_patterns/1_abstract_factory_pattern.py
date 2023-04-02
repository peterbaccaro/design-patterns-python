class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA:
    def method_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def method_a(self):
        return "ConcreteProductA1.method_a()"


class ConcreteProductA2(AbstractProductA):
    def method_a(self):
        return "ConcreteProductA2.method_a()"


class AbstractProductB:
    def method_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    def method_b(self):
        return "ConcreteProductB1.method_b()"


class ConcreteProductB2(AbstractProductB):
    def method_b(self):
        return "ConcreteProductB2.method_b()"


def client(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(product_a.method_a())
    print(product_b.method_b())


factory1 = ConcreteFactory1()
client(factory1)

factory2 = ConcreteFactory2()
client(factory2)
