import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
player_position_x = 400
player_position_y = 300
player_height = 50
player_width = 50


font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Game Over', True, RED)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Obstacle Game')
screen.fill(WHITE)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen, RED, (player_position_x, player_position_y, player_width, player_height))
    pygame.display.update()


