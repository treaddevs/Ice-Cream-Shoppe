# File which will implement the IceCreamShoppe class
# Created by Lindsay Jamieson
# 12/08/2022
# Implemented by Sam Treadwell

from Carton import Carton
from Scoop import Scoop

class IceCreamShoppe:
    '''Class IceCreamShoppe
        Attributes: carton_radius, carton_height, cartons_used
        Methods: serve, cartonsUsed'''

    def __init__(self, carton_radius, carton_height):
        self.carton_radius = carton_radius
        self.carton_height = carton_height
        self.carton = Carton(self.carton_radius, self.carton_height)
        self.cartons_used = 1
    # In the IceCreamShoppe class the carton object is defined and we start with 1 carton to scoop from
        '''Constructor
        Parameters: carton_radius, carton_height - dimensions for a carton
        Return: nothing'''
        pass

    def serve(self, numScoops, scooper):
        for i in range (len(numScoops)):
            if self.carton.hasEnoughFor(scooper):
                self.carton.remove(scooper)
            else:
                self.carton = Carton(self.carton_radius, self.carton_height)
                self.carton.remove(scooper)
                self.cartons_used += 1
    # The serve function implements the hasEnoughFor and remove functions and adds 
    # A carton each time the volume of the carton has been scooped out
        ''' serve method
        Parameters: numScoops - number of scoops wanted; 
            scooper - the specific Scoop to use
        Return: nothing'''
        pass

    def cartonsUsed(self):
        return self.cartons_used
    # The cartonsUsed function is a result of how many cartons have been used, as counted from serve 
    # Starting with 1 carton defined in "__init__"
        ''' cartonsUsed method
        Parameters: none
        Return: the number of cartons used so far in the Shoppe'''
        pass