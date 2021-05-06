import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)
player_size = 50
player_pos = [WIDTH / 2, HEIGHT - (2 * player_size)]

enemy_size = 50
enemy_pos = [100, 0]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Game Over', True, RED)


def checkCollision(rec1, rec2):
    collision = False
    while collision == False:
        if rec1.colliderect(rec2):
            screen.blit(text, (100, 100))
            collision = True
            print('Collision has occurred')
        break

    return


def print_and_break(item):
    i = 0
    for i in range(1):
        print(item)
        break


def draw_window():
    screen.fill(BACKGROUND_COLOR)
    rec1 = pygame.Rect(100, 300, 50, 50)
    rec2 = pygame.Rect(player_pos[0], player_pos[1], 50, 50)
    pygame.draw.rect(screen, RED, rec1)
    pygame.draw.rect(screen, BLUE, rec2)
    checkCollision(rec1, rec2)




run = True

while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x = x - player_size
            elif event.key == pygame.K_RIGHT:
                x = x + player_size
            elif event.key == pygame.K_UP:
                y = y - player_size
            elif event.key == pygame.K_DOWN:
                y = y + player_size

            player_pos = [x, y]
        draw_window()

    pygame.display.update()
