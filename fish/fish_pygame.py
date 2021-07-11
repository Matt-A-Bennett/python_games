import sys, pygame
import time
pygame.init()

path = '/home/mattb/code/python/python_flat/games/fish/'

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
fish = pygame.image.load(f"{path}fish_green.png")
fish = pygame.transform.scale(fish, (75, 75))
fishrect = fish.get_rect()
fishrect.y = 300

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    fishrect = fishrect.move(speed)
    if fishrect.left < 0 or fishrect.right > width:
        speed[0] = -speed[0]
    if fishrect.top < 0 or fishrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(fish, fishrect)
    pygame.display.flip()
    time.sleep(0.01)
