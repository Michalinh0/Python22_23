from points import Point

class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return (f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]")

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return (f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})")

    def __eq__(self, other):   # obsługa tr1 == tr2
        if not(isinstance(other, Triangle)):
            return False
        m1 = {self.pt1 , self.pt2 , self.pt3}
        m2 = {other.pt1 , other.pt2 , other.pt3}
        if(m1 == m2):
            return True
        return False
        # Trójkąty powinny być równe, jeżeli mają ten sam zbiór wierzchołków,
        # niezależnie od kolejności pt1, pt2, pt3.

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):           # zwraca środek (masy) trójkąta
        result = Point(0,0)
        result.x = (self.pt1.x + self.pt2.x + self.pt3.x ) / 3
        result.y = (self.pt1.y + self.pt2.y + self.pt3.y ) / 3
        return result

    def area(self):             # pole powierzchni
        return abs((self.pt1.x)*(self.pt2.y - self.pt3.y) + (self.pt2.x)*(self.pt3.y - self.pt1.y) + (self.pt3.x)*(self.pt1.y - self.pt2.y)) / 2

    def move(self, x, y):      # przesunięcie o (x, y)
        return Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y,self.pt3.x + x, self.pt3.y + y)

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Triangle(1,2,3,4,5,8)) , "[(1, 2), (3, 4), (5, 8)]")

    def test_repr(self):
        self.assertEqual(repr(Triangle(1,2,3,4,5,8)) , "Triangle(1, 2, 3, 4, 5, 8)")

    def test_equal(self):
        self.assertTrue(Triangle(1,2,3,4,5,8) == Triangle(1,2,3,4,5,8))
        self.assertTrue(Triangle(1,2,3,4,5,8) == Triangle(3,4,1,2,5,8))
        self.assertFalse(Triangle(1,2,3,4,5,8) == Triangle(1,2,3,4,5,7))

    def test_ne(self):
        self.assertFalse(Triangle(1,2,3,4,5,6) != Triangle(1,2,3,4,5,6))
        self.assertFalse(Triangle(1,2,3,4,5,6) != Triangle(3,4,1,2,5,6))
        self.assertTrue(Triangle(1,2,3,4,5,6) != Triangle(1,2,3,4,5,7))

    def test_center(self):
        self.assertEqual(Triangle(0,0,0,3,3,0).center() , Point(1,1))

    def test_area(self):
        self.assertTrue(Triangle(0,0,0,3,4,0).area() == 6)

    def test_move(self):
        self.assertEqual(Triangle(1,2,3,4,5,8).move(2,1) , Triangle(3,3,5,5,7,9))

if __name__ == '__main__':
    unittest.main()
    