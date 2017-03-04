import pygame, sys, time
from pygame.locals import *
WIDTH = 500
HEIGHT = 400
MIDDLE = (WIDTH/2,HEIGHT/2)
TOP_L = (0,0)
TOP_R = (WIDTH,0)
BOTTOM_L = (0,HEIGHT)
BOTTOM_R = (WIDTH,HEIGHT)
pygame.init()
UPLEFT = 'upleft'
windowSurface = pygame.display.set_mode(BOTTOM_R,0,32)
BLACK = (0,0,0)
WHITE = (255,255,255)
location = (250,200)
radius = 45
color = WHITE
border = 1

def Circle(surface, color, radius, location = MIDDLE, border = 1):
    pygame.draw.circle(surface, color, location,radius,border)
c1 = {'topx':250,'topy':200, 'color':WHITE, 'dir':UPLEFT}
Circle(windowSurface, color, radius, location, 1)
#last

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(BLACK)
    if c1['dir'] == UPLEFT:
        c1['topx'] -= 5
    pygame.draw.circle(windowSurface, color, (c1['topx'],c1['topy']),radius,border)
    pygame.display.update()
    time.sleep(0.02)
