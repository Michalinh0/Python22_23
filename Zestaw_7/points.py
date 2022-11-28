class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return(f"({self.x}, {self.y})")
        


    def __repr__(self):        # zwraca string "Point(x, y)"
        return(f"Point({self.x}, {self.y})")

    def __eq__(self, other):   # obsługa point1 == point2
        if not (isinstance(other,Point)):
            return False
        if (self.x == other.x and self.y == other.y):
            return True
        else:
            return False


    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        result = Point(0 , 0)
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

    def __sub__(self, other):   # v1 - v2
        result = Point(0 , 0)
        result.x = self.x - other.x
        result.y = self.y - other.y
        return result

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return (self.x * self.x + self.y * self.y)**(1/2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Point(2,5)) , "(2, 5)")

    def test_repr(self):
        self.assertEqual(repr(Point(2,5)) , "Point(2, 5)")

    def test_eq(self):
        self.assertFalse(Point(2 , 3) == Point(3 , 3))
        self.assertTrue(Point(2 , 3) == Point(2 , 3))
    
    def test_ne(self):
        self.assertTrue(Point(2 , 3) != Point(3 , 3))
        self.assertFalse(Point(2 , 3) != Point(2 , 3))

    def test_add(self):
        self.assertTrue(Point(2 , 3) + Point(3 , 2) == Point(5 , 5))

    def test_sub(self):
        self.assertTrue(Point(5 , 5) - Point(3 , 2) == Point(2 , 3))

    def test_mul(self):
        self.assertEqual(Point(3 , 3) * Point(4 , 4) , 24)

    def test_cross(self):
        self.assertEqual(Point(3 , 3).cross(Point(4 , 4)) , 0)
    
    def test_length(self):
        self.assertEqual(Point(3,4).length() , 5)

    def test_hash(self):
        self.assertEqual(hash(Point(0 , 1)) , -1950498447580522560)

if __name__ == '__main__':
    unittest.main()
    print(hash(Point(0 , 1)))