"""
this module create a car store that gets items from a car factory


+---------------+-------------+
| Making a table| Stuff in it |
+---------------+-------------+
| 1.            | Part 1      |
+---------------+-------------+
| 2.            | Part 2      |
+---------------+-------------+


"""

class Car:

    """
     a single  car class
     all car types


    """
    def __init__(self):
        """
        this is a car constructor.
        :param self: the instance of this object
        :type self: car

        """
        self.type = ""
        self.model = ""
        self.wheels = 4
        self.doors = 3
        self.seets = 5


    def print_model(self):
        """
        print the moudule of the current car using self.model and self.type.
        :param self: the instance of this object
        :type self:Car
        :return:nothing
        :rtype:none
        """
        print("This car is a {model}: {type}, Wow!".format(model=self.model,type= self.type))

    def print_space(self):
        """
        print the moudule of the current car using self.model and self.type.
        :param self: the instance of this object
        :type self:Car
        :return:nothing
        :rtype:none
        """
        print("The car has {0} doors and {1} seets".format(self.doors, self.seets))

    def __str__(self):
        """
        prints :
        This car is a {s.model}: {s.type}, Wow!
        The car has {s.doors} doors and {s.seets} seets
        :return: a custom string showing off thr make model and the capacity of the current car
        """
        return """
This car is a {s.model}: {s.type}, Wow!
The car has {s.doors} doors and {s.seets} seets""".format(s=self)


class BMW(Car):
    def __init__(self, **arg):

        """
        creates a BMW class.
        innherits Car

        :param arg: contains the information about BMW cars.
        :type arg: dict

        :param arg: the type of the car . shoud be part of arg . key is "type"
        :type type: str

        :param doors: the doors that the car has . should be a part of arg. key is "Doors"
        :type doors :int

        :param fuel: the fuel that the car has . should be a part of arg. key is "fuel"
        :type fuel: fuel

        """

        Car.__init__(self)
        self.model = "BMW"
        self.type = "{} Series".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")
class Mercedes(Car):
    def __init__(self, **arg):
        """
        creates a Mercedes class.
        innherits Car

        :param arg: contains the information about BMW cars.
        :type arg: dict

        :param arg: the type of the car . shoud be part of arg . key is "type"
        :type type: str

        :param doors: the doors that the car has . should be a part of arg. key is "Doors"
        :type doors :int

        :param fuel: the fuel that the car has . should be a part of arg. key is "fuel"
        :type fuel: fuel

        """



        Car.__init__(self)
        self.model = "Mercedes"
        self.type = "{} Class".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")


class Fuel:
    """
    the fuel of a car
    :param arg: the information about the fuel
    :type arg: dict

    :param liters: how many liters of fuel  needed
    :type liters: int

    :param type: what type of fuel needed
    :type type: str

    """
    def __init__(self, **arg):
        self.liters = arg.get("liters")
        self.type = arg.get("type")

    def __str__(self):
        return """It uses {s.liters}L of {s.type}¢.""".format(s=self)


class CarFactory:
    def __init__(self, **kwargs):
        self.car = kwargs.get("type")(type=kwargs.get("car_type"),doors=kwargs.get("doors"),fuel=Fuel(liters=kwargs.get("liters"),type=kwargs.get("fuel_type")))

    def get_car(self):
        """Returns a Mercedes"""
        return self.car


class CarStore:
    inventory = []

    def __init__(self, **kwargs):
        self._car_factory = CarFactory(type=kwargs.get("type"), car_type=kwargs.get("car_type"),doors=kwargs.get("doors"),liters=kwargs.get("liters"),fuel_type=kwargs.get("fuel_type"))
        self.inventory.append(self._car_factory.get_car())

    def show_car(self, car=None):
        """
        shows a car and what fuel it uses
        if car is not defined gets one for the factory

        :param car: a car to be displyed . default

        """


        if not car:
            car = self._car_factory.get_car()

        print(car)
        print(car.fuel)

    def show_inventory(self):
        for i in self.inventory:
            self.show_car(i)


    def __str__(self):
        return "".join([str(i) for i in self.inventory])


store = CarStore(type=Mercedes, car_type= "E", doors=2, liters = 2,fuel_type = "Disel")
store2 = CarStore(type=Mercedes, car_type= "C", doors=4, liters = 2,fuel_type = "Disel")
store3 = CarStore(type=BMW, car_type="1", doors= 3, liters= 2.5, fuel_type = "Gasoline")
store.show_inventory()

print("\n","-"*100)


class Lada(Car):
    def __init__(self, **arg):
        """
        creates a Lada class.
        innherits Car

        :param arg: contains the information about BMW cars.
        :type arg: dict

        :param arg: the type of the car . shoud be part of arg . key is "type"
        :type type: str

        :param doors: the doors that the car has . should be a part of arg. key is "Doors"
        :type doors :int

        :param fuel: the fuel that the car has . should be a part of arg. key is "fuel"
        :type fuel: fuel

        """


        Car.__init__(self)
        self.model = "Lada"
        self.type = "{}".format(arg.get("type"))
        self.doors = arg.get("doors")
        self.fuel = arg.get("fuel")

store = CarStore(type=Lada, car_type="VAZ-2107",doors=2,liters=1.2,fuel_type="Octane Gasoline")

store.show_inventory()




