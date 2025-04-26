"""
하이 스코어
"""
import pygame
import random 

pygame.init()

WIDTH = 500
ROWS = 20

win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake game")

FONT= pygame.font.SysFont("Arial", 30)

high_score = 0

def draw_grid(surface):
    size_btwn = WIDTH // ROWS
    for i in range(ROWS):
        x,y = size_btwn * i , size_btwn * i
        pygame.draw.line(surface, (255,255,255), (x,0), (x, WIDTH))
        pygame.draw.line(surface, (255,255,255), (0,y), (WIDTH, y))

def draw_score(surface, score, high_score):
    score_text = FONT.render(f"Score:{score}", True, (255,255,255))
    high_score_text = FONT.render(F"High Score:{high_score}", True, (255,255,255))
    surface.blit(score_text, (10,10))
    surface.blit(high_score_text, (10,40))

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
        self.score = 0
        
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

        #벽 충돌 확인
        if(self.dirnx == 1 and self.body[0].pos[0]>= ROWS) or \
            (self.dirnx == -1 and self.body[0].pos[0] < 0) or \
            (self.dirny == 1 and self.body[0].pos[1] >= ROWS) or \
            (self.dirny == -1 and self.body[0].pos[1] < 0):
                game_over(self.score)
        #자기 자신과 충돌하면 게임오버
        for i in range(1, len(self.body)):
            if self.body[0].pos==self.body[i].pos:
                game_over(self.score)
                break




    def addCube(self):
        """먹이를 먹으면 몸을 길게 추가"""
        tail = self.body[-1]
        new_cube = Cube((tail.pos[0] - self.dirnx, tail.pos[1] - self.dirny))
        self.body.append(new_cube)
        self.score += 10
        
    def reset(self,pos):
        """게임 리셋"""
        self.body = [Cube(pos)]
        self.dirnx, self.dirny = 0,1
        self.score = 0

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
        

def game_over(score):
    # print("game over")
    """게임 오보 화면"""

    global s, snack, high_score # 뱀과 먹이를 초기화를 위해 global 사용

    # 최고 점수 갱신
    if score > high_score:
        high_score = score

    win.fill((0,0,0))
    game_over_text = FONT.render(f"GameOver! Score:{score}", True, (255,255,255))
    high_score_text = FONT.render(f"High Score:{high_score}", True, (255,255,255))
    win.blit(high_score_text, (WIDTH//5, WIDTH //3+40))

    win.blit(game_over_text, (WIDTH//4, WIDTH //3))
    pygame.display.update()

    pygame.time.delay(2000)

    waiting = True 
    while waiting:
        for evenr in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

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
    draw_score(win, s.score, high_score)
    pygame.display.update()

pygame.quit()
