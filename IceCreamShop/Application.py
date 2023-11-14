# File which will hold the main function for the IceCreamShoppe project
# Created by Lindsay Jamieson
# 12/08/2022
# Implemented by Sam Treadwell

from IceCreamShoppe import IceCreamShoppe
from Carton import Carton
from Scoop import Scoop

def main():
    first_scoop = int(input("What is the radius of your first scooper? "))
    second_scoop = int(input("What is the radius of your second scooper? "))
    carton_radius = int(input("What is the radius of your carton? "))
    carton_height = int(input("What is the height of your carton? "))
# User is asked information pertaining to the radii of the first two scoops and the carton's radius and height
    ice_cream_shoppe = IceCreamShoppe(carton_radius, carton_height)
# The ice_cream_shoppe variable is assigned to the IceCreamShoppe Class
    scoop1 = Scoop(first_scoop)
    scoop2 = Scoop(second_scoop)
# Variables scoop1 and scoop2 are assigned to the first two scoops
    more = 1
# The more variable is the counter for more ice cream in the while loop
    more = int(input("Would you like more ice cream? (Enter 1 for yes and 0 for no): "))
    while more != 0:
        first_scoop_num = input("How many radius of " + str(first_scoop) + " scoops would you like? ")
        second_scoop_num = input("How many radius of " + str(second_scoop) + " scoops would you like? ")
# Program asks how many scoops of each size the user wants
        ice_cream_shoppe.serve(first_scoop_num, scoop1)
        ice_cream_shoppe.serve(second_scoop_num, scoop2)
# The ice_cream_shoppe variable assigns the method called serve based on the radii of each scoop 
# And the class Scoop creates each scoop object
        more = int(input("Would you like more ice cream? (Enter 1 for yes and 0 for no): "))
# Program asks if the user wants more ice cream and loop will prompt how many scoops of each size 
# The user wants if 1 is entered for yes
    print("You used " + str(ice_cream_shoppe.cartons_used) + " cartons of ice cream")
# Program ends when user enters 0 for more ice cream
# This ends the loop and prints out how many cartons of ice cream were used
main() 
