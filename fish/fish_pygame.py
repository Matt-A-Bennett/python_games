import sys, pygame
import time
pygame.init()

path = '/home/mattb/code/python/python_flat/games/fish/'

class Fish():
    def __init__(self, path, x_width, y_width):
        import sys, pygame
        import numpy as np
        self.size = np.random.randint(25, 124)
        color_ind = int(np.floor(self.size / 25)) - 1
        colors = ['red', 'orange', 'green', 'blue']
        self.image = pygame.image.load(f"{path}fish_{colors[color_ind]}.png")
        self.fish = self.image

        side = np.random.randint(1,5)
        if side == 1:
            self.fish = pygame.transform.flip(self.fish, True, False)
            self.rect = self.fish.get_rect()
            self.rect.y = np.random.randint(1,y_width)
            self.rect.x = 0
            self.speed = [np.random.randint(1, 5), 0]
        if side == 2:
            self.rect = self.fish.get_rect()
            self.rect.y = np.random.randint(1,y_width)
            self.rect.x = x_width
            self.speed = [-np.random.randint(1, 5), 0]
        if side == 3:
            self.fish = pygame.transform.rotate(self.fish, 270)
            self.rect = self.fish.get_rect()
            self.rect.x = np.random.randint(1,x_width)
            self.rect.y = y_width
            self.speed = [0, -np.random.randint(1, 5)]
        if side == 4:
            self.fish = pygame.transform.rotate(self.fish, 90)
            self.rect = self.fish.get_rect()
            self.rect.x = np.random.randint(1,x_width)
            self.rect.y = 0
            self.speed = [0, np.random.randint(1, 5)]

        self.fish = pygame.transform.scale(self.fish, (self.size, self.size))

    def update(self):
        self.rect = self.rect.move(self.speed)

x_width = 1920
y_width = 1080
n_fish = 20

black = 0, 0, 0
size = width, height = x_width, y_width
screen = pygame.display.set_mode(size)

test = Fish(path, x_width, y_width)
test.rect
test.update()

school_of_fish = []
for fish_idx in range(n_fish):
    school_of_fish.append(Fish(path, x_width, y_width))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    for fish_idx in range(n_fish):
        tmp_fish = school_of_fish[fish_idx]
        tmp_fish.update()
        if (tmp_fish.rect[0] < 0) or (tmp_fish.rect[0] > x_width) or (tmp_fish.rect[1] < 0) or (tmp_fish.rect[1] > y_width):
            school_of_fish[fish_idx] = Fish(path, x_width, y_width)

        screen.blit(tmp_fish.fish, tmp_fish.rect)

    pygame.display.flip()
    time.sleep(0.01)
