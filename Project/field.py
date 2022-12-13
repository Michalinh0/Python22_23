class Field:
    
    def __init__(self):
        self.clicked = False
        self.rightclicked = False
        self.bomb = False
        self.neighbouring_bombs = 0
        self.flagged = False

    def reveal(self):
        if self.clicked:
            return None
        if self.flagged:
            return "flag"
        self.clicked = True
        if self.bomb:
            return "mine"
        if self.neighbouring_bombs == 0:
            return "0"
        else:
            return "click"

    def flag(self):
        self.flagged = not self.flagged

    def setbomb(self):
        self.bomb = True

    def add_neighbouring_bomb(self):
        self.neighbouring_bombs += 1

    def image(self):
        if self.flagged:
            return "flag"
        if not self.clicked:
            return "clickable"
        if self.clicked and not self.bomb:
            return str(self.neighbouring_bombs)
        return "mine"

    def image_lost(self):
        if self.flagged and not self.bomb:
            return "wrong"
        else:
            return self.image()

    def getbomb(self):
        return self.bomb

    