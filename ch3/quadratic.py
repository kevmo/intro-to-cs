import math

def main():
    """This program computers the real solns to a quadratic"""

    a, b, c = input("Please enter the coefficients (a, b, c): ")

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print "The solutions are {0}, {1}".format(root1, root2)

main()
