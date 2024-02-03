import pygame
from random import randint

#  I don't know what to name this:
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
timer = 250

#  Circle:
radius = 15
ball_x = 500 - radius
ball_y = 300 - radius
n = randint(-1, 0)
m = randint(-1, 1)
if n == 0: n = 1

#  Players:
left_paddle_y = right_paddle_y = 200
left_paddle_vel = right_paddle_vel = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and left_paddle_y != 20:
                left_paddle_vel = -1
            if event.key == pygame.K_s and left_paddle_y + 200 != 590:
                left_paddle_vel = 1
            if event.key == pygame.K_UP and right_paddle_y != 20:
                right_paddle_vel = -1
            if event.key == pygame.K_DOWN and right_paddle_y + 200 != 590:
                right_paddle_vel = 1
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_w, pygame.K_s]:
                left_paddle_vel = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                right_paddle_vel = 0
    if ball_x > 1000 or ball_x < 0:
        ball_x = 500 - radius
        timer = 250
    
    if ball_y >= 575 or ball_y <= 20:
        m = -m
    left_paddle_y += left_paddle_vel
    right_paddle_y += right_paddle_vel
    ball_x += n
    ball_y += m
    if left_paddle_y >= 385:
        left_paddle_y = 385
    if left_paddle_y <= 20:
        left_paddle_y = 20
    if right_paddle_y >= 385:
        right_paddle_y = 385
    if right_paddle_y <= 20:
        right_paddle_y = 20
    
    if 0 <= ball_x <= 15:
        if left_paddle_y <= ball_y <= left_paddle_y + 200:
            n = -n; m = randint(0, 100) / 100
            timer += randint(1, 30)
            print('\a')
    if 985 <= ball_x <= 1000:
        if right_paddle_y <= ball_y <= right_paddle_y + 200:
            ball_x = 985
            n = -n; m = randint(0, 100) / 100
            timer += randint(1, 30)
            print('\a')

    screen.fill('black')
    pygame.draw.circle(screen, 'green', (ball_x, ball_y), radius)
    pygame.draw.rect(screen, 'blue', pygame.Rect(0, left_paddle_y, 15, 200))
    pygame.draw.rect(screen, 'red', pygame.Rect(985, right_paddle_y, 15, 200))
    pygame.draw.line(screen, 'yellow', (0, 15), (1000, 15), width = 10)
    pygame.draw.line(screen, 'yellow', (0, 585), (1000, 585), width = 10)
    pygame.display.update()
    clock.tick(timer)