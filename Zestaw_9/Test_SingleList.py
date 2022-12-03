import pytest
from SingleList import SingleList , Node

def test_adding():
    alist = SingleList()
    alist.insert_head(Node(11))
    alist.insert_head(Node(22))
    alist.insert_tail(Node(33))
    assert(alist.count() == 3)
    assert(alist.headcheck() == 22)
    assert(alist.tailcheck() == 33)

def test_deleting():
    alist = SingleList()
    alist.insert_head(Node(11))
    alist.insert_head(Node(22))
    alist.insert_tail(Node(33))
    alist.remove_head()
    alist.remove_tail()
    assert(alist.count() == 1)
    assert(alist.headcheck() == 11)
    assert(alist.tailcheck() == 11)

def test_empty():
    alist = SingleList()
    assert(alist.is_empty())
    alist.insert_head(Node(1))
    assert not (alist.is_empty())
    alist.remove_tail()
    assert(alist.is_empty())

def test_join():
    alist = SingleList()
    alist.insert_head(Node(11))
    alist.insert_head(Node(22))
    alist.insert_tail(Node(33))
    blist = SingleList()
    blist.insert_head(Node(1))
    blist.insert_head(Node(2))
    blist.insert_tail(Node(3))
    alist = alist.join(blist)
    assert(alist.count() == 6)
    assert(alist.headcheck() == 22)
    assert(alist.tailcheck() == 3)

if __name__ == "__main__":
    pytest.main()