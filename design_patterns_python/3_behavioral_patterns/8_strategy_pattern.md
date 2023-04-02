The Strategy pattern is a behavioral design pattern that allows a client object to choose from a family of algorithms at runtime. It encapsulates each algorithm in a separate class and makes them interchangeable at runtime.

In this example, `Strategy` is an abstract class that defines the interface for all algorithms. The `OperationAdd`, `OperationSubtract`, and `OperationMultiply` classes are concrete implementations of the `Strategy` class that encapsulate the addition, subtraction, and multiplication algorithms, respectively.

The Context class represents the client object that uses the strategy objects. It contains a reference to the current strategy object and uses its `execute_strategy` method to delegate the algorithm execution to the current strategy object.

In the `main` function, a `Context` object is created with an initial strategy of `OperationAdd`. The `execute_strategy` method of the `Context` object is called with two numbers, which returns the sum of the numbers. The same process is repeated with the other two strategies, which return the difference and product of the numbers, respectively.

This implementation of the Strategy pattern allows the client object to choose from a family of algorithms at runtime. It also encapsulates each algorithm in a separate class, which makes it easier to add or modify algorithms without affecting the other algorithms or the client object.
