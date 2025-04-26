import pygame

pygame.init()

WIDTH = 500
ROWS = 20

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake game step02")

def draw_grid(surface):
    size_btwn = WIDTH // ROWS
    for i in range(ROWS):
        x,y = size_btwn * i , size_btwn * i
        pygame.draw.line(surface, (255,255,255), (x,0), (x, WIDTH))
        pygame.draw.line(surface, (255,255,255), (0,y), (WIDTH, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win.fill((0,0,0))
    draw_grid(win)
    pygame.display.update()

pygame.quit()