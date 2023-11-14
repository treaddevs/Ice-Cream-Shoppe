# File which will hold the implementation of Scoop
# Created by Lindsay Jamieson
# 12/08/2022
# Implemented by Sam Treadwell

import math

class Scoop:
   '''Class Scoop
      Attributes: radius
      Methods: volume
   '''
   def __init__(self, radius):
         self.radius = radius
   # Here we assign the attribute radius to the scoop object we are creating
         '''Constructor - creates a new instance of Scoop
            Parameters -
               self - the current object
               radius - the radius of the scoop
         '''
   def volume(self):
      return ((4/3)*(math.pi)*((self.radius)** 3))
   # This formula defines the volume for a sphere which is the shape the scoop will create based on the radius size
      '''Method - calculate the volume of the scoop
         Parameters:
            self - the current object     
      '''