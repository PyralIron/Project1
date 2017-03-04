import pygame, sys
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

def Circle(surface, color, radius, location = MIDDLE, border = 1):
    pygame.draw.circle(surface, color, location,radius,border)
c1 = {'rect':pygame.Rect(200,200,20,20), 'color':WHITE, 'dir':UPLEFT}
Circle(windowSurface, color, radius, location, 1)
#last
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
