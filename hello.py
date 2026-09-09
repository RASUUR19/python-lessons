"""
The Earth can be approximated as a sphere with a radius of 6370 km.
Use the cell below to find out the volume of such a shape in cubic meters ( m3 ).
Hint: the volume  V  of a sphere with radius  r  is given by  V=43πr3 .
To get the value of  π  use math.pi after importing the math module
"""
import math
from fractions import Fraction
constant = Fraction(4, 3)
radius   = 6370 * 1000
Pie = round(math.pi, 4)
units = "m\u00B3"
answer = constant * Pie * radius ** 3
volume = str(answer) + units
print(volume)

print("OR")

import math
radius_km = 6370
radius_m = radius_km * 1000
pi = round(math.pi, 4)
volume = (4 / 3) * pi * radius_m ** 3
print("Pi:", pi)
print("Volume:", volume, "m³")