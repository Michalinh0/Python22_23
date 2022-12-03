import pytest
from stack import Stack

def test_push():
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert(stack.size == 5)
    assert(stack.peek() == 3)

def test_pop():
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert(stack.pop() == 3)
    assert(stack.count() == 2)

def test_full_exception():
    stack = Stack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    with pytest.raises(ValueError):
        stack.push(4)

def test_empty_exception():
    stack = Stack(3)
    with pytest.raises(ValueError):
        stack.pop()

if __name__ == "__main__":
    pytest.main()