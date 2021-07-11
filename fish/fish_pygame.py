import sys, pygame, os
import time
pygame.init()

path=os.getcwd() # Automaticlaly gets the current directory
path=path+"/" # adds / at the end of it. (might need to adapt for linux later)
#path = '/home/mattb/code/python/python_flat/games/fish/'
#path = 'C:/Users/canoluk/Desktop/GitHub/python_games/fish/'


class Fish():
    def __init__(self, path, x_width, y_width):
        import pygame
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

       
# Initial pop-up screen size
x_width = 500
y_width = 500
n_fish = 20

black = 10, 50, 100
size = width, height = x_width, y_width
screen = pygame.display.set_mode(size)

# basic font 
base_font = pygame.font.Font(None, 32)
base_font2=pygame.font.Font(None, 16)
user_text = '800'
user_text2= '600'


text = base_font.render('Screen Resolution', True, black)
text2 = base_font.render('Press ENTER', True, black)
text3 = base_font2.render('Width(pixels)', True, black)
text4 = base_font2.render('Height(pixels)', True, black)
textRect = pygame.Rect(150,150,140,32)
text2Rect= pygame.Rect(175,300,140,32)
text3Rect = pygame.Rect(120,210,140,32)
text4Rect= pygame.Rect(120,260,140,32)
  
# create rectangle
input_rect = pygame.Rect(200, 200, 140, 32)
input_rect2 = pygame.Rect(200, 250, 140, 32)

# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('lightskyblue3')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('chartreuse4')
color = color_passive

clock = pygame.time.Clock()

active1 = False
active2 = False
done = False

# Loop for the first input screen
while True:
    for event in pygame.event.get():
  
      # if user types QUIT then the screen will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active1 = True
            else:
                active1 = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect2.collidepoint(event.pos):
                active2 = True
            else:
                active2 = False
            
                
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RETURN:
                    done=True
            
            if active1:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    done=True
            # Unicode standard is used for string
            # formation
                else:
                    user_text += event.unicode
            if active2:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                # get text input from 0 to -1 i.e. end.
                    user_text2 = user_text2[:-1]
                elif event.key == pygame.K_RETURN:
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
    pygame.draw.rect(screen, color1, input_rect)
    pygame.draw.rect(screen, color2, input_rect2)
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
    pygame.display.flip()
      
    # clock.tick(60) means that for every second at most
    # 60 frames should be passed.
    clock.tick(60)
    if done:
        break




x_width=int(user_text)
y_width=int(user_text2)
size = width, height = x_width, y_width
screen = pygame.display.set_mode(size)

test = Fish(path, x_width, y_width)
test.rect
test.update()

school_of_fish = []
for fish_idx in range(n_fish):
    school_of_fish.append(Fish(path, x_width, y_width))

pygame.mixer.init() # Initialize music mixer
pygame.mixer.music.load("guiles-theme.mp3") # Load background music
pygame.mixer.music.play(-1,0,0) # Starts playing music. (loops, maxtime, fade_ms)
                                # If loops input is -1, it keeps looping forever.


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE: # Quits when you press ESCAPE
                pygame.quit()
                sys.exit()

    screen.fill(black)
    for fish_idx in range(n_fish):
        tmp_fish = school_of_fish[fish_idx]
        tmp_fish.update()
        if (tmp_fish.rect[0] < 0) or (tmp_fish.rect[0] > x_width) or (tmp_fish.rect[1] < 0) or (tmp_fish.rect[1] > y_width):
            school_of_fish[fish_idx] = Fish(path, x_width, y_width)

        screen.blit(tmp_fish.fish, tmp_fish.rect)

    pygame.display.flip()
    time.sleep(0.01)
