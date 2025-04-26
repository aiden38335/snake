import pygame

pygame.init()

WIDTH = 500
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake game step01")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win.fill((0,0,0))
    pygame.display.update()

pygame.quit()