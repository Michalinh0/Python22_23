class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie

class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        #return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(1)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):   # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node_removed = self.tail
        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            while node.next.next != None:
                node = node.next
            node.next = None
            self.tail = node
            self.length -= 1
            return node_removed

    def join(self,other):
        if not isinstance(other , SingleList):
            raise ValueError("other jest zlego typu")
        self.tail.next = other.head
        self.tail = other.tail
        self.length += other.length
        return self
    
    def clear(self):
        self.length = 0
        self.head = self.tail = None

    def headcheck(self): #Interfejs do testowania poprawności działania (wartość heada)
        return self.head.data

    def tailcheck(self): #Interfejs do testowania poprawności działania (wartość taila)
        return self.tail.data