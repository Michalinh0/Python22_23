from field import Field
import random
import time

class Board:

    def __init__(self, height , width , bombs):
        self.height = height
        self.width = width
        self.bombs = bombs
        self.lost = False
        self.nonbombs = height * width - bombs
        self.available_flags = bombs
        self.prepare()

    def prepare(self):
        self.game_area = list()
        for i in range(self.height):
            row = list()
            for j in range(self.width):
                field = Field()
                row.append(field)
            self.game_area.append(row)
        self.put_bombs()

    def put_bombs(self):
        bomb_locations = random.sample(range(0 , self.height * self.width) , self.bombs)
        #print(bomb_locations)
        for i in range(self.height):
            for j in range(self.width):
                if(i*self.height + j in bomb_locations):
                    self.game_area[i][j].setbomb()
                    self.fill_neighbours(i,j)

    def fill_neighbours(self , x , y):
        
        if(x != 0 and y != 0): # NW
            self.game_area[x-1][y-1].add_neighbouring_bomb()
        if(x != 0): # N
            self.game_area[x-1][y].add_neighbouring_bomb()
        if(x != 0 and y < self.width - 1): # NE
            self.game_area[x-1][y+1].add_neighbouring_bomb()
        if(y < self.width - 1): # E
            self.game_area[x][y+1].add_neighbouring_bomb()
        if(x < self.height - 1 and y < self.width - 1): # SE
            self.game_area[x+1][y+1].add_neighbouring_bomb()
        if(x < self.height - 1): # S
            self.game_area[x+1][y].add_neighbouring_bomb()
        if(x < self.height - 1 and y != 0): # SW
            self.game_area[x+1][y-1].add_neighbouring_bomb()
        if(y != 0): # W
            self.game_area[x][y-1].add_neighbouring_bomb()

    def handle_click(self , x , y , rightclick):
        if(rightclick and self.available_flags != 0):
            self.game_area[x][y].flag()
        else:
            res = self.reveal(x,y)

    def reveal(self , x , y):
        res = self.game_area[x][y].reveal()
        #print(res ,x, y)
        if res == "click" or res == "0":
            self.nonbombs -= 1
        if res == "mine":
            self.lost = True
            self.lose()
        if res == "0":
            if(x != 0 and y != 0): # NW
                self.reveal(x-1 , y-1)
            if(x != 0): # N
                self.reveal(x-1,y)
            if(x != 0 and y < self.width - 1): # NE
                self.reveal(x-1,y+1)
            if(y < self.width - 1): # E
                self.reveal(x,y+1)
            if(x < self.height - 1 and y < self.width - 1): # SE
                self.reveal(x+1,y+1)
            if(x < self.height - 1): # S
                self.reveal(x+1,y)
            if(x < self.height - 1 and y != 0): # SW
                self.reveal(x+1,y-1)
            if(y != 0): # W
                self.reveal(x,y-1)
        
    def win(self):
        return self.nonbombs == 0

    def getlost(self):
        return self.lost

    def lose(self):
        for i in self.game_area:
            for j in i:
                if(not j.clicked and j.getbomb()):
                    j.reveal()




    



'''
Code for later:

bomb_locations = random.sample(range(0 , self.height * self.width) , self.bombs)
        print(bomb_locations)

if(i*self.height + j in bomb_locations):
    field.setbomb()
    self.fill_neighbours(i,j)

'''