import pygame

pygame.init()
screen = pygame.display.set_mode((600, 480))
pygame.display.set_caption('Stickman Dungeon Adventure')
running = True
while running:


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

