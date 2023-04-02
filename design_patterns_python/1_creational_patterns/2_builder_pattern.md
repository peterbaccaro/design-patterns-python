The Builder pattern is a creational design pattern that separates the construction of a complex object from its representation, allowing the same construction process to create different representations. In Python, this pattern can be implemented using classes and interfaces.

In this example, `Director` is a class that directs the construction process using a builder object. `Builder` is an abstract class that defines the interface for building the product object. `Product` is the complex object being built.

`CarBuilder` and `TruckBuilder` are concrete builder classes that implement the `Builder` interface and build different representations of the `Product` object. They override the `set_engine` method to enforce engine type constraints.

The `client` function creates a `Director` object and two builder objects (`CarBuilder` and `TruckBuilder`). It then directs the construction process using each builder object to create a different representation of the `Product` object. The resulting products are printed to the console.

This implementation of the Builder pattern allows for a flexible construction process and easy switching between different representations of the same complex object.
