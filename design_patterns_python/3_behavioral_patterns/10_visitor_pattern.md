The Visitor pattern is a behavioral design pattern that allows adding new operations to an existing class hierarchy without modifying the classes themselves.

In this example, `Visitor` is an abstract class that defines a set of operations that can be performed on the Shape objects. The `Shape` class is an abstract class that defines an accept method, which takes a visitor object as a parameter. The `Circle` and `Square` classes inherit from the `Shape` class and implement the `accept` method.

Two concrete `Visitor` classes, `DrawVisitor` and `PrintVisitor`, inherit from the `Visitor` class and implement the operations defined in the abstract class. The `DrawVisitor` class draws shapes, and the `PrintVisitor` class prints shapes.

In the main function, a list of `Shape` objects is created, and two visitor objects, `DrawVisitor` and `PrintVisitor`, are instantiated. The `accept` method is called on each shape object with both visitors as parameters. This way, each shape object accepts the two visitors, and the appropriate method in each visitor is called for each shape.

This implementation of the Visitor pattern allows adding new operations to the `Shape` hierarchy without modifying the `Shape` classes themselves. It also keeps related behavior in separate classes, making the code easier to maintain and extend.
