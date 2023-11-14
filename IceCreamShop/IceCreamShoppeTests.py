''' Project 8 - Ice Cream Shoppe Tests
    Classes tested: Scoop, Carton
    CS 5001 - Fall 2022
    Sam Treadwell
    12/10/2022
'''

import math
import unittest

from Scoop import Scoop
from Carton import Carton

class ScoopTest(unittest.TestCase):
    def test_init(self):
        scoop = Scoop(radius=2)
        self.assertEqual(scoop.radius, 2)
# The scoop object has the set radius 2 so the object's attribute radius should equal 2
    def test_volume(self):
        scoop = Scoop(radius=2)
        scoop.volume = ((4/3)*(math.pi)*((scoop.radius)** 3))
        self.assertAlmostEqual(scoop.volume, 33.51)
# The scoop object's volume is defined by the sphere equation
# With radius = 2 it rounds out approximately 33.51 so it should be AlmostEqual to this number
class CartonTest(unittest.TestCase):
    def test_init(self):
        carton = Carton(radius=4, height=8)
        self.assertEqual(carton.radius, 4)
        self.assertEqual(carton.height, 8)
# When the carton object's paramenters radius and height are set to 4 and 8 they should equal these numbers
        carton.carton_volume = (((math.pi*(carton.radius)**2))*carton.height)
        self.assertAlmostEqual(carton.carton_volume, 402.12)
# When the carton object's radius = 4, height = 8 the carton_volume should be almost equal to 402.123859
def main():
    unittest.main(verbosity = 3)
main()