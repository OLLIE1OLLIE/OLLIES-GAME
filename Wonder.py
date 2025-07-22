import random
import pygame, os, sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((450, 600))
#Loading are Sprites for later...
Player = pygame.image.load(os.path.join('Ghost.png')).convert()
Block = pygame.image.load(os.path.join('Block.png')).convert()

# Every variable needed for the program
Player_x = 225
Player_y = 300
px_dir = 0
py_dir = 0
speed = 2
Block_x = random.randint(1, 450)
Block_y = 0
bx_dir = 0
by_dir = 0
speed = 2
Part_1 = True
run = True
# My loop for the game so it can run.
while run:
    
    screen.fill('White')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(Player (Player_x, Player_y))
# This updates the display
    pygame.display.flip
pygame.quit
sys.exit()