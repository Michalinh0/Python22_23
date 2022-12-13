import pygame
import os
import time

class Game:

    def __init__(self , board):
        self.board = board
        self.piece_size = (40 , 40)
        self.screen_width = self.piece_size[0] * board.width
        self.screen_height = self.piece_size[1] * board.height + 100
        self.screen_size = self.screen_width, self.screen_height
        self.images = self.load_images()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 100)
        sound_played = False
        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rightclick = pygame.mouse.get_pressed()[2]
                    self.handle_click(position,rightclick)
                    #print(self.board.nonbombs)
                    if(not sound_played and self.board.getlost()):
                        pygame.mixer.Sound("explosion.mp3").play()
                        sound_played = True
            self.draw()
            pygame.display.flip()
            if(self.board.won):
                pygame.mixer.Sound("win.mp3").play()
                time.sleep(10)
                running = False

    
    def load_images(self):
        sprites = dict()
        for i in os.listdir("sprites"):
            sprite = pygame.image.load(os.path.join("sprites" , i))
            sprite = pygame.transform.scale(sprite , self.piece_size)
            sprites[i.split(".")[0]] = sprite
        return sprites
        

    def draw(self):
        self.screen.fill((245, 245 , 220))
        position = (0,100)
        for i in range(self.board.height):
            for j in range(self.board.width):
                if not self.board.lost:
                    image = self.images[self.board.game_area[i][j].image()]
                else:
                    image = self.images[self.board.game_area[i][j].image_lost()]
                self.screen.blit(image , position)
                #print(position)
                position = position[0] + self.piece_size[0] , position[1] 
            position = 0 , position[1] + self.piece_size[1]
        if(not self.board.lost and not self.board.won):
            self.tick = pygame.time.get_ticks()
        text = f"{self.tick // 1000}.{round(self.tick // 100 % 10, 1)}"
        text = self.font.render(text , True , (0 , 0 , 0))
        text_rect = text.get_rect(center = (self.screen_size[0] // 2 , 50))
        self.screen.blit(text , text_rect)

    def handle_click(self , position , rightclick):
        pygame.mixer.Sound("click.mp3").play()
        if(self.board.lost):
            return
        position = position[0] , position[1] - 100
        #print(position , rc)
        x = position[1] // self.piece_size[1]
        y = position[0] // self.piece_size[0]
        #print(x,y)
        if(position[0] >= 0 and position[1] >= 0):
            self.board.handle_click(x , y , rightclick)



