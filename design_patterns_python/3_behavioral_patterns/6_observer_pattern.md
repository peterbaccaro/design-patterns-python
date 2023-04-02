The Observer pattern is a behavioral design pattern that allows one-to-many relationships between objects. In this pattern, when one object (the subject) changes state, all of its dependents (observers) are notified and updated automatically.

In this example, `Observer` is a class that represents an observer that can receive updates from the subject. `Subject` is a class that represents a subject that can be observed by multiple observers. Observers can attach and detach themselves from the subject, and the subject can notify all of its observers when its state changes.

The `main` function creates a `Subject` object and three `Observer` objects. It attaches all three observers to the subject, then notifies them with a message. It then detaches the second observer from the subject, and notifies the remaining observers with another message.

This implementation of the Observer pattern allows you to create a one-to-many relationship between objects, where the subject can notify multiple observers of its state changes. It also keeps the details of the subject's state changes encapsulated within the subject, and allows you to add or remove observers without affecting the subject or the other observers.
