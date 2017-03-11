import pygame, sys, time, math
from pygame.locals import *
from math import *

WIDTH = 1000
HEIGHT = 800
MIDDLE = (WIDTH/2,HEIGHT/2)
TOP_L = (0,0)
TOP_R = (WIDTH,0)
BOTTOM_L = (0,HEIGHT)
BOTTOM_R = (WIDTH,HEIGHT)
pygame.init()
CWISE = 'clockwise'
CCWISE = 'counterclockwise'
windowSurface = pygame.display.set_mode(BOTTOM_R,0,32)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,200,50)
RED = (200,4,53)
BLUE = (0,34,200)
PURPLE = (200,0,200)
location = (250,200)
radius = 5
color = WHITE
border = 5
speed = 0.1
sun = (500,400)
x = 0
y = 0
def Circle(surface, color, radius, location = MIDDLE, border = 1):
    pygame.draw.circle(surface, color, location,radius,border)

c1 = {'centerx':500,'centery':400, 'color':WHITE, 'dir':CWISE, 'angle':0,'radius':200}
c2 = {'centerx':500,'centery':400, 'color':GREEN, 'dir':CWISE, 'angle':90,'radius':100}
c3 = {'centerx':500,'centery':400, 'color':RED, 'dir':CWISE, 'angle':180,'radius':300}
c4 = {'centerx':500,'centery':400, 'color':BLUE, 'dir':CWISE, 'angle':45,'radius':240}
c5 = {'centerx':500,'centery':400, 'color':PURPLE, 'dir':CWISE, 'angle':56,'radius':400}
Circle(windowSurface, color, radius, location, 1)
#last
def revolve(myangle,direction,centerx,centery,myspeed,mycolor,myradius):
    if direction == CWISE:
        myangle += myspeed
        x = floor(cos(myangle)*myradius)+centerx
        y = floor(sin(myangle)*myradius)+centery
    if direction == CCWISE:
        myangle -= myspeed
        x = floor(cos(myangle)*myradius)+centerx
        y = floor(sin(myangle)*myradius)+centery
        
    pygame.draw.circle(windowSurface, mycolor, (x,y),radius,border)
    return (myangle)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(BLACK)
    (myangle) = revolve(c1['angle'],c1['dir'],c1['centerx'],c1['centery'],speed,c1['color'],c1['radius'])
    c1['angle'] = myangle
    (myangle) = revolve(c2['angle'],c2['dir'],c2['centerx'],c2['centery'],speed,c2['color'],c2['radius'])
    c2['angle'] = myangle
    (myangle) = revolve(c3['angle'],c3['dir'],c3['centerx'],c3['centery'],speed,c3['color'],c3['radius'])
    c3['angle'] = myangle
    (myangle) = revolve(c4['angle'],c4['dir'],c4['centerx'],c4['centery'],speed,c4['color'],c4['radius'])
    c4['angle'] = myangle
    (myangle) = revolve(c5['angle'],c5['dir'],c5['centerx'],c5['centery'],speed,c5['color'],c5['radius'])
    c5['angle'] = myangle
    pygame.display.update()
    time.sleep(0.02)
