"""
Contains the classes used in this exersise
"""

class Car:
    """A Simple Car Class"""
    def __init__(self):
        self.type = ""
        self.model = ""
        self.wheels = 4
        self.doors = 3
        self.seets = 5

    def print_model(self):
        print("This car is a {model}: {type}, Wow!".format(model=self.model,type= self.type))

    def print_space(self):
        print("The car has {0} doors and {1} seets".format(self.doors, self.seets))

    def __str__(self):
        return """
This car is a {s.model}: {s.type}, Wow!
The car has {s.doors} doors and {s.seets} seets""".format(s=self)


class BMW(Car):
    """A BMW Car"""
    def __init__(self, **arg):
          Car.__init__(self)
          self.model = "BMW"
          self.type = "{} Series".format(arg.get("type"))
          self.doors = arg.get("doors")
          self.fuel = arg.get("fuel")

class Mercedes(Car):
    """A Mercedes Car"""
    def __init__(self, **arg):
        Car.__init__(self)
        self.model = "Mercedes"
        self.type = "{} Class".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")


class Fuel:
    def __init__(self, **arg):
        self.liters = arg.get("liters")
        self.type = arg.get("type")

    def __str__(self):
        return """It uses {s.liters}L of {s.type}¢.""".format(s=self)


