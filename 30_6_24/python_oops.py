class Dog:
    attr1 = "mammal"

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is a {}".format(Tommy.__class__.attr1))

# Instance attributes (object)
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

# Accessing class methods
Rodger.speak()
Tommy.speak()

# Inheritance
# Capability of one class to derive/inherit the properties from another class
# Base/Parent class --> Derived/Child class

