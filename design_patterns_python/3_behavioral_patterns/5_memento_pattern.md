The Memento pattern is a behavioral design pattern that allows you to capture and store the current state of an object in a way that you can restore it later. In Python, this pattern can be implemented using classes and interfaces.

In this example, Memento is a class that stores the state of an Originator object. Originator is a class that creates and restores Mementos and has a state that can be saved and restored. Caretaker is a class that manages Mementos and can restore the state of an Originator object to a previous state.

The main function creates an Originator object with an initial state of "State1". It then creates a Caretaker object and adds a Memento to it that stores the current state of the Originator object. It changes the state of the Originator object to "State2" and adds another Memento to the Caretaker object. It then changes the state of the Originator object to "State3".

The Originator object then restores its state from the first Memento in the Caretaker object, which sets its state back to "State1". It then restores its state from the second Memento in the Caretaker object, which sets its state back to "State2".

This implementation of the Memento pattern allows you to capture and store the current state of an object in a way that you can restore it later. It also keeps the details of the object's state encapsulated within the object, and allows you to add new types of Mementos to the system without affecting the existing Mementos or the Originator object.
