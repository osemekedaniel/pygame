import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255,0,0)
player_pos = [400,300]
player_size = 50

screen = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = True

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
	    pygame.quit()
            sys.exit()
    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    pygame.display.update()

