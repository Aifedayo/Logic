"""
A function for calculating the volume of a Sphere
"""

def vol_of_sphere(rad):
    return ((4/3)*(3.14)*(rad**3))

vol_of_sphere(int(input('Enter the radius of the sphere: ')))

"""
OR
"""
from math import pi
def vol_of_sphere2(rad):
    return ((4/3)*(pi)*(rad**3))

vol_of_sphere2(int(input('Enter the radius of the sphere: ')))