import random

class RandomQueue:

    def __init__(self):
        self.items = list()
        self.count = 0

    def insert(self, item):
        self.items.append(item)
        self.count +=1

    def remove(self): # zwraca losowy element
        if(self.is_empty()):
            raise ValueError("Kolejka jest pusta")
        rand = random.randint(0,self.elements() - 1)
        self.count -=1
        return self.items.pop(rand)
        
    def is_empty(self): 
        return self.count == 0

    def is_full(self):
        return False

    def clear(self):  # czyszczenie listy
        self.items = list()

    def elements(self):
        return self.count