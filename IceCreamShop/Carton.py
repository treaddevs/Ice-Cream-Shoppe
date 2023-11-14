# File which will hold the implementation of Carton
# Created by Lindsay Jamieson
# 12/08/2022
# Implemented by Sam Treadwell

import math
from Scoop import Scoop

class Carton:
    ''' Class: Carton
        Attributes: contains
        Methods: hasEnoughFor, remove'''
    
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.carton_volume = (((math.pi*(self.radius)**2))*self.height)
    # The carton object is a cylinder-shaped object which is based on the attributes of radius and height
    # The attribute carton_volume implements the formula for the carton's cylinder shape
        ''' Constructor
            Parameters:
                self
                radius - radius of a carton
                height - height of a carton'''

    def hasEnoughFor(self, scoop):
        if scoop.volume() < self.carton_volume:
            return True
        else:
            return False
    # Here if the volume of the scoop is less then the volume of the carton there is enough to make a scoop
    # Otherwise it returns False
        ''' hasEnoughFor
            Parameters:
                scoop - the Scoop to be used on the Carton
            Return:
                whether or not the Carton contains enough to make a Scoop'''
 
    def remove(self, scoop):
        self.carton_volume = self.carton_volume - scoop.volume()
    # If the volume of the carton allows for the scoop to fit, then we remove the scoop's volume
    # Adjusting the new volume of the carton object to reflect the change
        ''' remove
            Parameters:
                scoop - the Scoop to be used on the Carton
        '''
