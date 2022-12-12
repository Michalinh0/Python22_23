import pygame
from pygame import RESIZABLE
import os

class Game:

    def __init__(self , board):
        self.board = board
        self.piece_size = (40 , 40)
        self.screen_size = self.piece_size[0] * board.height, self.piece_size[1] * board.width + 100
        self.images = self.load_images()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        running = True
        while(running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    rc = pygame.mouse.get_pressed()[2]
                    self.handle_click(position,rc)
            self.draw()
            pygame.display.flip()

    
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
                image = self.images[self.board.game_area[i][j].image()]
                self.screen.blit(image , position)
                position = position[0] + self.piece_size[0] , position[1]
            position = 0 , position[1] + self.piece_size[1]

    def handle_click(self , position , rc):
        position = position[0] , position[1] - 100
        print(position , rc)
        x = position[1] // self.piece_size[1]
        y = position[0] // self.piece_size[0]
        print(x,y)
        if(position[0] >= 0 and position[1] >= 0):
            self.board.handle_click(x , y , rc)



