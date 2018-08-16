"""
.. info: Alexander

The program is made to demonstrate api calls using requests.

"""
import requests
import json

class Street:
    """
    Class that holds the methods and the variables for the street that is beeing searched.

    :var int incidents: the incident counter.
    :var str url: holds the API url
    """
    #: incidents is set to 0
    incidents = 0
    url = "https://data.police.uk/api/crimes-at-location?date={date}&lat={coor[0]}&lng={coor[1]}"

    def __init__(self):
        self.name=""
        self.coor=[]

    def get_incedents_year(self):
        """
        | The incident gatherer.
        | It increments **incidents** for every month of the year.

        :arg self: to use local variables
        """
        for i in range(1,12):
            response = requests.get(self.url.format(date="2018-{:02d}".format(i),coor=self.coor)).content.decode()
            if response != "[]" and response != "":
                     self.incidents += len(json.loads(response))

    def __str__(self):
        """
        .. warning:: this only returns a string for the print function, it does not print the object.


        :returns str: The string to be printed when printing the class.

        """

        return """{} has {} incidents the year of 2018""".format(self.name,self.incidents)

class BakerStreet(Street):

    def __init__(self, **kwargs):
        """
        The constructor.

        :arg str name: The name of the street
        :arg str coor: can take a coordinate
        """
        Street.__init__(self)
        self.name = "221 Baker Street"
        self.coor = (51.523767,-0.1607444)
        self.incidents = 0

class PrivetDrive(Street):

    def __init__(self, **kwargs):
        """
        The constructor.

        :arg str name: The name of the street
        :arg str coor: can take a coordinate

        """
        Street.__init__(self)
        self.name = "4 Privet Drive"
        self.coor = (51.4110113, -2.6063299)
        self.incidents = 0


def get_all_Incodents():
    """
    Gets the incodents for all streets

    :returns tuple streets: Street objects with all incidents counted.

    """
    a = BakerStreet()
    b = PrivetDrive()
    a.get_incedents_year()
    b.get_incedents_year()
    return a,b


[print(i) for i in get_all_Incodents()]