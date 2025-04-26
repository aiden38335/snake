"""
뱀의 길이가 3칸(머리 + 몸 2개)로 시작하고, 자연스럽게 움직인다.
방향키를 누르면 뱀의 머리가 움직이고, 몸이 따라온다.
"""
import pygame

pygame.init()

WIDTH = 500
ROWS = 20

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake game step05")

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
    
    def move(self, dirnx, dirny):
        """뱀을 이동시키는 함수"""
        self.dirnx, self.dirny = dirnx, dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
    
    def draw(self,surface):
        """뱀 그리기"""
        dis = WIDTH // ROWS
        i,j = self.pos
        pygame.draw.rect(surface, self.color, (i * dis, j * dis, dis, dis))

class Snake:
    """뱀을 관리하는 클래스"""
    def __init__(self, color, pos):
        self.body = [Cube(pos)] # 뱀의 머리 추가
        self.dirnx, self.dirny = 0, 1 # 기본 이동 방향(아래쪽)
        
        # 미리 몸 2개 추가 (테스트용)
        self.body.append(Cube((pos[0]-1, pos[1])))
        self.body.append(Cube((pos[0]-2, pos[1])))
    
    def move(self):
        """뱀 이동"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.dirnx, self.dirny = -1, 0
        elif keys[pygame.K_RIGHT]:
            self.dirnx, self.dirny = 1, 0
        elif keys[pygame.K_UP]:
            self.dirnx, self.dirny = 0, -1
        elif keys[pygame.K_DOWN]:
            self.dirnx, self.dirny = 0, 1
        
        for i in range(len(self.body)-1 , 0, -1):
            self.body[i].pos = self.body[i-1].pos
        
        self.body[0].move(self.dirnx, self.dirny) # 머리 이동
        
    def draw(self, surface):
        """뱀 그리기"""
        for cube in self.body:
            cube.draw(surface)

        

s = Snake((255,0,0), (10,10)) # 뱀 생성

running = True
while running:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        
    
    s.move()
    win.fill((0,0,0))
    draw_grid(win)
    s.draw(win) # 뱀 그리기
    pygame.display.update()

pygame.quit()