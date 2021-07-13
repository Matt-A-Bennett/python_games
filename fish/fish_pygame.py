import sys, os, time
import pygame as pg
import numpy as np
pg.init()

path=os.getcwd() # Automaticlaly gets the current directory
path=path+"/" # adds / at the end of it. (might need to adapt for linux later)
#path = '/home/mattb/code/python/python_flat/games/fish/'
#path = 'C:/Users/canoluk/Desktop/GitHub/python_games/fish/'

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
            self.rect.x = -150
            self.speed = [np.random.rand()*5, 0]
        if side == 2:
            self.rect = self.fish.get_rect()
            self.rect.y = np.random.randint(1,height)
            self.rect.x = width
            self.speed = [-np.random.rand()*5, 0]
        if side == 3:
            self.fish = pg.transform.rotate(self.image, 270)
            self.rect = self.fish.get_rect()
            self.rect.x = np.random.randint(1,width)
            self.rect.y = height
            self.speed = [0, -np.random.rand()*5]
        if side == 4:
            self.fish = pg.transform.rotate(self.image, 90)
            self.rect = self.fish.get_rect()
            self.rect.x = np.random.randint(1,width)
            self.rect.y = -150
            self.speed = [0, np.random.rand()*5]

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

background_color = 10, 50, 100
n_fish = 20
friction_coef = 0.98

# basic font
base_font = pg.font.Font(None, 32)
base_font2=pg.font.Font(None, 16)
user_text = '800'
user_text2= '600'

screen = pg.display.set_mode([int(user_text), int(user_text2)])

text = base_font.render('Screen Resolution', True, background_color)
text2 = base_font.render('Press ENTER', True, background_color)
text3 = base_font2.render('Width(pixels)', True, background_color)
text4 = base_font2.render('Height(pixels)', True, background_color)
textRect = pg.Rect(150,150,140,32)
text2Rect= pg.Rect(175,300,140,32)
text3Rect = pg.Rect(120,210,140,32)
text4Rect= pg.Rect(120,260,140,32)

# create rectangle
input_rect = pg.Rect(200, 200, 140, 32)
input_rect2 = pg.Rect(200, 250, 140, 32)

# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pg.Color('lightskyblue3')

# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pg.Color('chartreuse4')
color = color_passive

clock = pg.time.Clock()

active1 = False
active2 = False
done = False

# Loop for the first input screen
while True:
    for event in pg.event.get():

      # if user types QUIT then the screen will close
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active1 = True
            else:
                active1 = False
        #if event.type == pg.MOUSEBUTTONDOWN:
            if input_rect2.collidepoint(event.pos):
                active2 = True
            else:
                active2 = False

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_RETURN:
                    done=True

            if active1:
                # Check for backspace
                if event.key == pg.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                elif event.key == pg.K_RETURN:
                    done=True
            # Unicode standard is used for string
            # formation
                else:
                    user_text += event.unicode
            if active2:
                # Check for backspace
                if event.key == pg.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                    user_text2 = user_text2[:-1]
                elif event.key == pg.K_RETURN:
                    done=True
            # Unicode standard is used for string
            # formation
                else:
                    user_text2 += event.unicode

    # it will set background color of screen
    screen.fill((255, 255, 255))

    if active1:
        color1 = color_active
    else:
        color1 = color_passive

    if active2:
        color2 = color_active
    else:
        color2 = color_passive

    # draw rectangle and argument passed which should
    # be on screen
    pg.draw.rect(screen, color1, input_rect)
    pg.draw.rect(screen, color2, input_rect2)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    text_surface2= base_font.render(user_text2, True, (255, 255, 255))

    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    screen.blit(text_surface2, (input_rect2.x+5, input_rect2.y+5))
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)
    screen.blit(text3, text3Rect)
    screen.blit(text4, text4Rect)
    # set width of textfield so that text cannot get
    # outside of user's text input

    input_rect.w = max(100, text_surface.get_width()+10)
    input_rect2.w = max(100, text_surface2.get_width()+10)

    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pg.display.flip()

    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)
    if done:
        break

width=int(user_text)
height=int(user_text2)
screen = pg.display.set_mode([width, height])

# Keys are automatically set to released every millisecond. This means we stop
# accelerating the player fish as soon as the key is released
pg.key.set_repeat(1)

pg.mixer.init() # Initialize music mixer
pg.mixer.music.load("guiles-theme.wav") # Load background music
pg.mixer.music.play(-1,0,0) # Starts playing music. (loops, maxtime, fade_ms)
                                # If loops input is -1, it keeps looping forever.

player = FishPlayer(path)

school_of_fish = []
for fish_idx in range(n_fish):
    school_of_fish.append(Fish_AI(path, width, height))

# GAME LOOP
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE: # Quits when you press ESCAPE
                pg.quit()
                sys.exit()

    screen.fill(background_color)

    # update all the AI fish
    for fish_idx in range(n_fish):
        tmp_fish = school_of_fish[fish_idx]
        tmp_fish.update()
        if (tmp_fish.rect[0] < -150) or (tmp_fish.rect[0] > width) or (tmp_fish.rect[1] < -150) or (tmp_fish.rect[1] > height):
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
