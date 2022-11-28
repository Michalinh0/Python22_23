from points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        if(self.area()==0):
            raise Exception ("Three points provided are collinear")

    def __str__(self):          # "[(x1, y1), (x2, y2), (x3, y3)]"
        return (f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]")

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return (f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})")

    def __eq__(self, other):    # obsługa tr1 == tr2
        if not(isinstance(other, Triangle)):
            return False
        m1 = {self.pt1 , self.pt2 , self.pt3}
        m2 = {other.pt1 , other.pt2 , other.pt3}
        if(m1 == m2):
            return True
        return False

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):           # zwraca środek trójkąta
        result = Point(0,0)
        result.x = (self.pt1.x + self.pt2.x + self.pt3.x ) / 3
        result.y = (self.pt1.y + self.pt2.y + self.pt3.y ) / 3
        return result

    def area(self):             # pole powierzchni
        return abs((self.pt1.x)*(self.pt2.y - self.pt3.y) + (self.pt2.x)*(self.pt3.y - self.pt1.y) + (self.pt3.x)*(self.pt1.y - self.pt2.y)) / 2

    def move(self, x, y):       # przesunięcie o (x, y)
        return Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y,self.pt3.x + x, self.pt3.y + y)

    def make4(self):            # zwraca krotkę czterech mniejszych
        ab = Point((self.pt1.x + self.pt2.x)/2 , (self.pt1.y + self.pt2.y)/2)
        bc = Point((self.pt2.x + self.pt3.x)/2 , (self.pt2.y + self.pt3.y)/2)
        ca = Point((self.pt3.x + self.pt1.x)/2 , (self.pt3.y + self.pt1.y)/2)
        t1 = Triangle(self.pt1.x , self.pt1.y , ab.x , ab.y , ca.x , ca.y)
        t2 = Triangle(self.pt2.x , self.pt2.y , ab.x , ab.y , bc.x , bc.y)
        t3 = Triangle(self.pt3.x , self.pt3.y , bc.x , bc.y , ca.x , ca.y)
        t4 = Triangle(ab.x , ab.y , bc.x , bc.y , ca.x , ca.y)
        return (t1 , t2  , t3 , t4)
#     A       po podziale    A
#    / \                    / \
#   /   \                  +---+
#  /     \                / \ / \
# C-------B              C---+---B

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
        self.assertFalse(Triangle(1,2,3,4,5,7) != Triangle(1,2,3,4,5,7))
        self.assertFalse(Triangle(1,2,3,4,5,7) != Triangle(3,4,1,2,5,7))
        self.assertTrue(Triangle(1,2,3,4,5,8) != Triangle(1,2,3,4,5,7))

    def test_center(self):
        self.assertEqual(Triangle(0,0,0,3,3,0).center() , Point(1,1))

    def test_area(self):
        self.assertTrue(Triangle(0,0,0,3,4,0).area() == 6)

    def test_move(self):
        self.assertEqual(Triangle(1,2,3,4,5,8).move(2,1) , Triangle(3,3,5,5,7,9))

    def test_make4(self):
        self.assertEqual(Triangle(0,0,4,0,0,4).make4() , (Triangle(0,0,2,0,0,2) , Triangle(4,0,2,0,2,2) , Triangle(0,4,2,2,0,2) , Triangle(2,0,2,2,0,2)))

if __name__ == '__main__':
    unittest.main() 