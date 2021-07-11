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

class FishPlayer():
    def __init__(self, path):
        import sys, pygame
        self.size = 50
        self.image = pygame.image.load(f"{path}fish_player.png")
        self.speed = [0, 0]
        self.facing = 'left'
        self.fish = self.image
        self.fish = pygame.transform.scale(self.fish, (self.size, self.size))
        self.rect = self.fish.get_rect()
        self.rect.x = 400
        self.rect.y = 300

    def update(self):
        import sys, pygame
        if self.speed[0] > 0 and self.facing == 'left' or self.speed[0] < 0 and self.facing == 'right':
            x = self.rect.x
            y = self.rect.y
            self.fish = pygame.transform.flip(self.fish, True, False)
            self.rect = self.fish.get_rect()
            self.rect.x = x
            self.rect.y = y
            if self.facing == 'left':
                self.facing = 'right'
            else:
                self.facing = 'left'
        self.rect = self.rect.move(self.speed)

x_width = 1920
y_width = 1080
n_fish = 20
background_color = 10, 50, 100

size = width, height = x_width, y_width
screen = pygame.display.set_mode(size)
pygame.key.set_repeat(1)

player = FishPlayer(path)

school_of_fish = []
for fish_idx in range(n_fish):
    school_of_fish.append(Fish(path, x_width, y_width))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(background_color)

    # update all the AI fish
    for fish_idx in range(n_fish):
        tmp_fish = school_of_fish[fish_idx]
        tmp_fish.update()
        if (tmp_fish.rect[0] < 0) or (tmp_fish.rect[0] > x_width) or (tmp_fish.rect[1] < 0) or (tmp_fish.rect[1] > y_width):
            school_of_fish[fish_idx] = Fish(path, x_width, y_width)
        screen.blit(tmp_fish.fish, tmp_fish.rect)

    # alter speed in repsonse to keypresses
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.speed[1] -= 0.2
            if event.key == pygame.K_DOWN:
                player.speed[1] += 0.2
            if event.key == pygame.K_RIGHT:
                player.speed[0] += 0.2
            if event.key == pygame.K_LEFT:
                player.speed[0] -= 0.2

    # impose max speed
    if player.speed[0] > 8:
        player.speed[0] = 8
    if player.speed[0] < -8:
        player.speed[0] = -8
    if player.speed[1] > 8:
        player.speed[1] = 8
    if player.speed[1] < -8:
        player.speed[1] = -8

    # add some friction
    player.speed[0] -= (player.speed[0] - 0)/100
    player.speed[1] -= (player.speed[1] - 0)/100

    player.update()
    screen.blit(player.fish, player.rect)

    pygame.display.flip()
    time.sleep(0.01)
