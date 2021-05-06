  import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255,0,0)
BACKGROUND_COLOR = (0,0,0)
player_pos = [400,300]
player_size = 50

screen = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = True

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x = x- player_size
            elif event.key == pygame.K_RIGHT:
                x = x + player_size
            player_pos = [x,y]
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
    pygame.display.update()

