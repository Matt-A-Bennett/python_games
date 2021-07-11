import sys, pygame
import time
pygame.init()

class Fish():
    def __init__(self, size=20, speed=1, x=0, y=50, color='r'):
        self.size = size
        self.speed = speed
        self.x = x
        self.y = y
        self.color = color

size = width, height = 800, 600
speed = [2, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("fish/block.png")
ballrect = ball.get_rect()
ballrect.y = 300
ballrect.move
fish = []
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(0.01)
