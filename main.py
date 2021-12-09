import pygame
import random
pygame.init()
pygame.display.set_caption('snake')
def end_game():
    print('your final score was: ' + str(len(prevx)))
    pygame.quit()
    exit()
    exit()
sizex = 300
sizey = 300
window = pygame.display.set_mode((sizex, sizey))
clock = pygame.time.Clock()
rect = pygame.Rect(0, 0, 20, 20)
rect.center = window.get_rect().center
applex = 0
appley = 0
def make_apple():
    global prevx
    global prevy
    global applex
    global appley
    global sizex
    global sizey
    run = True
    while run:
        applex = (random.randint(0, ((sizex) - 10) / 10)) * 10
        appley = (random.randint(0, ((sizey) - 10) / 10)) * 10
        if len(prevx) > 0:
            for step in range(len(prevx)):
                if prevx[step] == applex and prevy[step] == appley:
                    pass
                else:
                    run = False
        else:
            run = False
    pygame.draw.rect(window, (255, 255, 255),
    pygame.Rect(applex, appley, 10, 10))
run = True
up = False
down = False
left = False
right = False
x = sizex / 2
y = sizey / 2
flip = False
moving = False
prevx = []
prevy = []
moved = False
make_apple()
while run:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'up' and not down:
                up = True
                down = False
                left = False
                right = False
                moved = True
            if pygame.key.name(event.key) == 'down' and not up:
                down = True
                up = False
                left = False
                right = False
                moved = True
            if pygame.key.name(event.key) == 'left' and not right:
                left = True
                up = False
                down = False
                right = False
                moved = True
            if pygame.key.name(event.key) == 'right' and not left:
                right = True
                up = False
                down = False
                left = False
                moved = True
    if up:
        if y == 0:
            end_game()
        y -= 10
    if down:
        if y == sizey - 10:
            end_game()
        y += 10
    if left:
        if x == 0:
            end_game()
        x -= 10
    if right:
        if x == sizex - 10:
            end_game()
        x += 10
    for step in range(len(prevx)):
        if prevx[step] == x and prevy[step] == y and moved:
            end_game()
    if moved or len(prevx) == 0:
        prevx.append(x)
        prevy.append(y)
    for step in range(len(prevx)):
        pygame.draw.rect(window, (255, 255, 255),
                         pygame.Rect(prevx[step], prevy[step], 10, 10))
    if applex == x and appley == y:
        make_apple()
    elif moved:
        del prevx[0]
        del prevy[0]
    pygame.draw.rect(window, (255, 255, 255),
    pygame.Rect(applex, appley, 10, 10))
    pygame.display.flip()
    window.fill(0)
end_game()
