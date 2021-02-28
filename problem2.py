#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""

#Distance = sqry((x1 - x2)**2 + (y1-y2)**2)
import math
def distance(x1,y1,x2,y2):
    dist = (|(x1-x2)**2 + (y1-y2)**2)
