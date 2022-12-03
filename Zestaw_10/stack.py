class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if(self.is_full()):
            raise ValueError("stos jest pelny")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if(self.is_empty()):
            raise ValueError("stos jest pusty")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None    # usuwam referencję
        return data

    def peek(self): #Interfejs do testowania poprawności działania (podejrzenie ostatniego elementu)
        return self.items[self.n-1]

    def count(self): #Interfejs do testowania poprawności działania (sprawdzenie ilości elementów na stosie)
        return self.n