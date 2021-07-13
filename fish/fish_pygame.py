import sys
import pygame as pg
import numpy as np
import time
pg.init()

class Fish_AI():
    def __init__(self, path, width, height):
        self.size = np.random.randint(25, 124)
        color_ind = int(np.floor(self.size / 25)) - 1
        colors = ['red', 'orange', 'green', 'blue']
        self.image = pg.image.load(f"{path}fish_{colors[color_ind]}.png")
        self.fish = self.image

        side = np.random.randint(1,5)
        if side == 1:
            self.fish = pg.transform.flip(self.image, True, False)
            self.rect = self.fish.get_rect()
            self.rect.y = np.random.randint(1,height)
            self.rect.x = 0
            self.speed = [np.random.randint(1, 5), 0]
        if side == 2:
            self.rect = self.fish.get_rect()
            self.rect.y = np.random.randint(1,height)
            self.rect.x = width
            self.speed = [-np.random.randint(1, 5), 0]
        if side == 3:
            self.fish = pg.transform.rotate(self.image, 270)
            self.rect = self.fish.get_rect()
            self.rect.x = np.random.randint(1,width)
            self.rect.y = height
            self.speed = [0, -np.random.randint(1, 5)]
        if side == 4:
            self.fish = pg.transform.rotate(self.image, 90)
            self.rect = self.fish.get_rect()
            self.rect.x = np.random.randint(1,width)
            self.rect.y = 0
            self.speed = [0, np.random.randint(1, 5)]

        self.fish = pg.transform.scale(self.fish, (self.size, self.size))

    def update(self):
        self.rect = self.rect.move(self.speed)

class FishPlayer():
    def __init__(self, path):
        self.size = 50
        self.image = pg.image.load(f"{path}fish_player.png")
        self.fish = pg.transform.scale(self.image, (self.size, self.size))
        self.speed = [0, 0]
        self.max_speed = 8
        self.acceleration = 0.1
        self.facing = 'left'
        self.rect = self.fish.get_rect()
        self.rect.x = 400
        self.rect.y = 300

    def update(self):
        if self.speed[0] > 0 and self.facing == 'left' or self.speed[0] < 0 and self.facing == 'right':
            x = self.rect.x
            y = self.rect.y
            self.fish = pg.transform.flip(self.fish, True, False)
            self.rect = self.fish.get_rect()
            self.rect.x = x
            self.rect.y = y
            if self.facing == 'left':
                self.facing = 'right'
            else:
                self.facing = 'left'
        self.rect = self.rect.move(self.speed)

path = '/home/mattb/code/python/python_flat/games/fish/'

width = 1920
height = 1080
background_color = 10, 50, 100
n_fish = 20
friction_coef = 0.98

screen = pg.display.set_mode([width, height])
pg.key.set_repeat(1)

player = FishPlayer(path)

school_of_fish = []
for fish_idx in range(n_fish):
    school_of_fish.append(Fish_AI(path, width, height))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and (event.key == pg.K_q or event.key == pg.K_ESCAPE)):
            sys.exit()

    screen.fill(background_color)

    # update all the AI fish
    for fish_idx in range(n_fish):
        tmp_fish = school_of_fish[fish_idx]
        tmp_fish.update()
        if (tmp_fish.rect[0] < 0) or (tmp_fish.rect[0] > width) or (tmp_fish.rect[1] < 0) or (tmp_fish.rect[1] > height):
            school_of_fish[fish_idx] = Fish_AI(path, width, height)
        screen.blit(tmp_fish.fish, tmp_fish.rect)

    # alter speed in repsonse to keypresses
    pg.event.pump()
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and player.speed[1] > -player.max_speed:
                player.speed[1] -= player.acceleration
            if event.key == pg.K_DOWN and player.speed[1] < player.max_speed:
                player.speed[1] += player.acceleration
            if event.key == pg.K_RIGHT and player.speed[0] < player.max_speed:
                player.speed[0] += player.acceleration
            if event.key == pg.K_LEFT and player.speed[0] > -player.max_speed:
                player.speed[0] -= player.acceleration

    # add some friction
    player.speed[0] = player.speed[0]*friction_coef
    player.speed[1] = player.speed[1]*friction_coef

    player.update()
    screen.blit(player.fish, player.rect)

    pg.display.flip()
    time.sleep(0.01)
