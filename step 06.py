import pygame
import random 

pygame.init()

WIDTH = 500
ROWS = 20\

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake game step06")

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
        #self.body.append(Cube((pos[0]-1, pos[1])))
        #self.body.append(Cube((pos[0]-2, pos[1])))
    
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

    def addCube(self):
        """먹이를 먹으면 몸을 길게 추가"""
        tail = self.body[-1]
        new_cube = Cube((tail.pos[0] - self.dirnx, tail.pos[1] - self.dirny))
        self.body.append(new_cube)
        
    def draw(self, surface):
        """뱀 그리기"""
        for cube in self.body:
            cube.draw(surface)

def randomSnack(snake):
    """랜덤 위치에 먹이 생성(뱀과 겹치지 않도록)"""
    while True:
        x, y = random.randrange(ROWS), random.randrange(ROWS)
        is_valid = True

        for cube in snake.body:
            if cube.pos == (x, y):
                is_valid = False 
                break 
        
        if is_valid:
            return x,y
        

s = Snake((255,0,0), (10,10)) # 뱀 생성
snack = Cube(randomSnack(s), color=(0,0,255))

running = True
while running:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        
    
    s.move()

    if s.body[0].pos == snack.pos:
        s.addCube()
        snack = Cube(randomSnack(s), color=(0,0,225))

    win.fill((0,0,0))
    draw_grid(win)
    s.draw(win) # 뱀 그리기
    snack.draw(win)
    pygame.display.update()

pygame.quit()
