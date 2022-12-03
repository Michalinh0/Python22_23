import pytest
from queue import Queue

def test_basic_operations():
    q = Queue(5)
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    assert(q.get() == 1)
    assert(q.get() == 2)
    assert(q.get() == 3)
    assert(q.get() == 4)

def test_empty_exception():
    q = Queue(5)
    with pytest.raises(ValueError):
        q.get()

def test_full_exception():
    q = Queue(3)
    q.put(1)
    q.put(2)
    q.put(3)
    with pytest.raises(ValueError):
        q.put(4)

if __name__ == "__main__":
    pytest.main()