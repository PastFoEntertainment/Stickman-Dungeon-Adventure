import pygame
from pygame import FULLSCREEN

from images_import import icon

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1920, 1080), FULLSCREEN)
pygame.display.set_caption('Stickman Dungeon Adventure')
pygame.display.set_icon(icon())
menu = True
game = False

while menu:
    pygame.draw.rect(screen, 'Blue', (860, 515, 200, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 200 < x < 400 and 200 <= y <= 250:
                game = True
                menu = False
    clock.tick(30)
    pygame.display.update()

while game:

    f = open('Levels/Floor_1.txt')
    y = 0
    for row in f:
        x = 0
        for obj in row:
            if obj == '0':
                pygame.draw.rect(screen, 'Yellow', (x + 1, y, 40, 40))
            elif obj == '-':
                pygame.draw.rect(screen, 'Brown', (x + 1, y, 40, 40))
            elif obj == 'H':
                pygame.draw.rect(screen, 'Brown', (x + 1, y, 40, 40))
                pygame.draw.rect(screen, 'Red', (x + 1, y, 40, 40), 5)
            x += 40
        y += 40
    f.close()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    pygame.display.update()
    clock.tick(30)