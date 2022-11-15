class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return("(%d, %d", self.x , self.y)
        


    def __repr__(self): pass        # zwraca string "Point(x, y)"

    def __eq__(self, other):   # obsługa point1 == point2
        return self ==  other

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other): pass  # v1 + v2

    def __sub__(self, other): pass  # v1 - v2

    def __mul__(self, other): pass  # v1 * v2, iloczyn skalarny, zwraca liczbę

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self): pass          # długość wektora

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):
    point = Point(1,2)
    print(point.__str__())