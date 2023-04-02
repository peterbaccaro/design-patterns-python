The Bridge pattern is a structural design pattern that separates an abstraction from its implementation, allowing them to vary independently. In Python, this pattern can be implemented using classes and interfaces.

In this example, `Abstraction` is a class that represents the abstraction and delegates its implementation to an `Implementation` object. `Implementation` is an abstract class that defines the interface for the implementation.

`ConcreteImplementationA` and `ConcreteImplementationB` are concrete classes that inherit from `Implementation` and provide their own implementations of `operation_implementation`.

The `main` function creates two `Implementation` objects (`implementationA` and `implementationB`) and two `Abstraction` objects (`abstractionA` and `abstractionB`). Each `Abstraction` object is initialized with a different `Implementation` object.

`operation` is called on each `Abstraction` object, which in turn calls `operation_implementation` on its corresponding `Implementation` object. The output of each call is printed to the console.

This implementation of the Bridge pattern separates the abstraction from its implementation, allowing them to vary independently. It also allows new abstractions and implementations to be added without affecting the existing code.
