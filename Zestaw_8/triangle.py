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

    def from_points(p1 , p2 , p3):
        return Triangle(p1.x , p1.y , p2.x , p2.y , p3.x , p3.y)

    @property
    def top(self) -> float:
        return max(self.pt1.y , self.pt2.y, self.pt3.y)
    
    @property
    def left(self) -> float:
        return min(self.pt1.x , self.pt2.x, self.pt3.x)

    @property
    def bottom(self) -> float:
        return min(self.pt1.y , self.pt2.y, self.pt3.y)

    @property
    def right(self) -> float:
        return max(self.pt1.x , self.pt2.x, self.pt3.x)

    @property
    def width(self) -> float:
        return abs(self.right - self.left)

    @property
    def height(self) -> float:
        return abs(self.top - self.bottom)

    @property
    def topleft(self) -> Point:
        return Point(self.left , self.top)

    @property
    def topright(self) -> float:
        return Point(self.right , self.top)

    @property
    def bottomleft(self) -> float:
        return Point(self.left , self.bottom)

    @property
    def bottomright(self) -> float:
        return Point(self.right , self.bottom)

    