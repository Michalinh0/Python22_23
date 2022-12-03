import pytest
from randomqueue import RandomQueue

def test_add():
    q = RandomQueue()
    q.insert(2)
    q.insert(4)
    q.insert(6)
    q.insert(8)
    assert(q.elements() == 4)

def test_remove():
    q = RandomQueue()
    q.insert(2)
    q.insert(4)
    q.insert(6)
    q.insert(8)
    possible_values = [2,4,6,8]
    assert(q.remove() in possible_values)

def test_empty_exception():
    q = RandomQueue()
    with pytest.raises(ValueError):
        q.remove()

if __name__ == "__main__":
    pytest.main()