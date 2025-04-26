"""
뱀 움직이기
"""
import pygame

pygame.init()

WIDTH = 500
ROWS = 20

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake game step04")

def draw_grid(surface):
    size_btwn = WIDTH // ROWS
    for i in range(ROWS):
        x,y = size_btwn * i , size_btwn * i
        pygame.draw.line(surface, (255,255,255), (x,0), (x, WIDTH))
        pygame.draw.line(surface, (255,255,255), (0,y), (WIDTH, y))

class Cube:
    """뱀의 머리를 만드는 클래스"""
    def __init__(self, pos, color=(255,0,0)):
        self.pos = pos
        self.dirnx, self.dirny = 0,1 # 기본 이동 방향 (아래)
        self.color = color
    
    def move(self):
        """뱀을 이동시키는 함수"""
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
    
    def draw(self,surface):
        """뱀 그리기"""
        dis = WIDTH // ROWS
        i,j = self.pos
        pygame.draw.rect(surface, self.color, (i * dis, j * dis, dis, dis))
    
snake = Cube((10,10)) # 뱀의 위치 설정
        
running = True
while running:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.dirnx, snake.dirny = -1, 0
    elif keys[pygame.K_RIGHT]:
        snake.dirnx, snake.dirny = 1, 0
    elif keys[pygame.K_UP]:
        snake.dirnx, snake.dirny = 0, -1
    elif keys[pygame.K_DOWN]:
        snake.dirnx, snake.dirny = 0, 1
        
    
    snake.move()
    win.fill((0,0,0))
    draw_grid(win)
    snake.draw(win) # 뱀 그리기
    pygame.display.update()

pygame.quit()