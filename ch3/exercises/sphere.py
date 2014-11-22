import math
from sys import argv


rad = int(argv[1])

def volume(r):
    return math.pi * (4/3) * (r ** 3)

def area(r):
    return 4 * math.pi * (r ** 2)

print "The volume of the sphere  with radius {} is {}".format(rad, volume(rad))

print "The surface area of the sphere  with radius {} is {}".format(rad, area(rad))

