import pygame
from images_import import icon


pygame.init()
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption('Stickman Dungeon Adventure')
pygame.display.set_icon(icon())
menu = True
game = False

while menu:
    pygame.draw.rect(screen, 'Blue', (200, 200, 200, 50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 200 < x < 400 and 200 <= y <= 250:
                game = True
                menu = False

while game:
    screen.fill('White')
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()