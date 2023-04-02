The Decorator pattern is a structural design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.

In this example, `Component` is the interface that all components implement, and `ConcreteComponent` is the base component that we want to decorate. `Decorator` is the base decorator class that follows the same interface as the `Component` class, and `ConcreteDecoratorA` and `ConcreteDecoratorB` are the concrete decorators that add functionality to the `ConcreteComponent`.

The `Decorator` class takes an instance of `Component` as a parameter in its constructor. The `operation` method of `Decorator` calls the `operation` method of the component it wraps, and can add functionality before or after that method call.

When a client calls the `operation` method on a decorated component, it calls the decorated component's `operation` method, which in turn calls the next decorator's `operation` method, and so on, until the last decorator calls the `operation` method of the base `ConcreteComponent`.
