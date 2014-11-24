# Find the slope of two points

from sys import argv

script, x1, y1, x2, y2 = argv

p1 = (float(x1), float(y1))
p2 = (float(x2), float(y2))

def slope(point1, point2):
    rise = p2[1] - p1[1]
    run = p2[0] - p1[0]
    return rise/run

print slope(p1, p2)
