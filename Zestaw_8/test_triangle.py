from triangle import Triangle
from points import Point
import pytest

def test_str():
    x = str(Triangle(1,2,3,4,5,8))
    y = "[(1, 2), (3, 4), (5, 8)]"
    assert(x == y)

def test_repr():
    x = repr(Triangle(1,2,3,4,5,8))
    y = "Triangle(1, 2, 3, 4, 5, 8)"
    assert(x == y)

def test_equal():
    assert (Triangle(1,2,3,4,5,8) == Triangle(1,2,3,4,5,8))
    assert (Triangle(1,2,3,4,5,8) == Triangle(3,4,1,2,5,8))
    assert not (Triangle(1,2,3,4,5,8) == Triangle(1,2,3,4,5,7))

def test_ne():
    assert not (Triangle(1,2,3,4,5,8) != Triangle(1,2,3,4,5,8))
    assert not (Triangle(1,2,3,4,5,8) != Triangle(3,4,1,2,5,8))
    assert  (Triangle(1,2,3,4,5,8) != Triangle(1,2,3,4,5,7))

def test_center():
    triangle = Triangle(0,0,0,3,3,0)
    center = triangle.center()
    assert (center == Point(1,1))

def test_area():
    triangle = Triangle(0,0,0,3,4,0)
    assert (triangle.area() == 6)

def test_move():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.move(2,1) == Triangle(3,3,5,5,7,9))

def test_make4():
    triangle = Triangle(0,0,4,0,0,4)
    assert (triangle.make4() == (Triangle(0,0,2,0,0,2) , Triangle(4,0,2,0,2,2) , Triangle(0,4,2,2,0,2) , Triangle(2,0,2,2,0,2)))

def test_top():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.top == 8)

def test_left():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.left == 1)

def test_bottom():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.bottom == 2)

def test_right():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.right == 5)

def test_width():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.width == 4)

def test_height():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.height == 6)

def test_topleft():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.topleft == Point(1,8))

def test_topright():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.topright == Point(5,8))

def test_bottomleft():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.bottomleft == Point(1,2))

def test_bottomright():
    triangle = Triangle(1,2,3,4,5,8)
    assert (triangle.bottomright == Point(5,2))

if __name__ == "__main__":
    pytest.main()