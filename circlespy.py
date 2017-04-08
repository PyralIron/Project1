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
YELLOW = (200,200,0)
RAND = (100,100,100)
location = (250,200)
radius = 5
color = WHITE
border = 5
speed = 0.1
sun = (500,400)
G = 3.026757*(10**(-11))
x = 0
y = 0
def Circle(surface, color, radius, location = MIDDLE, border = 1):
    pygame.draw.circle(surface, color, location,radius,border)

c1 = {'name':"Earth",'loc':(700,350),'centerx':500,'centery':400, 'color':WHITE, 'dir':CWISE, 'angle':0,'radius':100, 'speed':0.3,'mass': 1.317, 'velocity':[-10,50]}
c2 = {'name':"c2",'loc':(250,400),'centerx':500,'centery':400, 'color':GREEN, 'dir':CWISE, 'angle':90,'radius':325, 'speed':0.05, 'mass': 1.073, 'velocity':[-20,60]}
c3 = {'name':"c3",'loc':(350,900),'centerx':500,'centery':400, 'color':RED, 'dir':CWISE, 'angle':180,'radius':350, 'speed':0.01, 'mass': 418, 'velocity':[-50,30]}
c4 = {'name':"c4",'loc':(450,200),'centerx':500,'centery':400, 'color':BLUE, 'dir':CWISE, 'angle':45,'radius':400, 'speed':0.01, 'mass':19.14, 'velocity':[10,50]}
c5 = {'name':"c5",'loc':(900,100),'centerx':500,'centery':400, 'color':PURPLE, 'dir':CWISE, 'angle':56,'radius':50, 'speed':0.5, 'mass':.00289, 'velocity':[10,50]}
c6 = {'name':"c6",'loc':(500,400),'centerx':500,'centery':400, 'color':YELLOW, 'dir':CWISE, 'angle':56,'radius':5, 'speed':0.001, 'mass':438500, 'velocity':[0,0]}
planetlist = (c1,c2,c3,c4,c5,c6)
def CenterofMass(planetlist):
    centerOfMassX = 0
    centerOfMassY = 0
    totalMass = 0
    for i in planetlist:
        totalMass += i['mass']
    for i in planetlist:
        centerOfMassX += i['mass']*i['loc'][0]
        centerOfMassY += i['mass']*i['loc'][1]
    centerOfMassX *= 1/totalMass
    centerOfMassY *= 1/totalMass
    pygame.draw.circle(windowSurface, RAND, (floor(centerOfMassX),floor(centerOfMassY)),10,1)
    print (centerOfMassX,centerOfMassY)
    return (centerOfMassX,centerOfMassY,totalMass)
Circle(windowSurface, color, radius, location, 1)
CenterofMass(planetlist)
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
def velocity(i,theplanetlist):
    centerOfMass = CenterofMass(theplanetlist)
    force = G*centerOfMass[2]*i['mass']/((centerOfMass[0]-i['loc'][0])**2+(centerOfMass[1]-i['loc'][1])**2)
    accel = force/i['mass']
    displacementX = i['loc'][0]-centerOfMass[0]
    displacementY = i['loc'][1]-centerOfMass[1]
    displacement = sqrt(displacementX**2+displacementY**2)
    accelX = displacement*accel/displacementX 
    accelY = displacement*accel/displacementY
    accelVec = (accelX,accelY)
    newVelX = (i['velocity'][0]+accelVec[0])/50
    newVelY = (i['velocity'][1]+accelVec[1])/50
    newVel = (newVelX,newVelY)
    print ('accel')
    print (i['name'])
    print (accelVec)
    i['velocity'] = newVel
    print ("velocity" + str(i['velocity'][0]) + "," + str(i['velocity'][1]))
    positionX = i['loc'][0]+newVel[0]
    positionY = i['loc'][1]+newVel[1]
    position = (positionX,positionY)
    i['loc'] = position
    print ("position"+str(i['loc'][0]) + "," + str(i['loc'][1]))
    print ("-------------------------------------")
    Circle(windowSurface, color, radius, (floor(i['loc'][0]),floor(i['loc'][1])), 1)
    return(i['loc'])
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(BLACK)
    velocity(c1,planetlist)
    velocity(c2,planetlist)
    velocity(c3,planetlist)
    velocity(c4,planetlist)
    velocity(c5,planetlist)
    velocity(c6,planetlist)
    (myangle) = revolve(c1['angle'],c1['dir'],c1['centerx'],c1['centery'],c1['speed'],c1['color'],c1['radius'])
    c1['angle'] = myangle
    (myangle) = revolve(c2['angle'],c2['dir'],c2['centerx'],c2['centery'],c2['speed'],c2['color'],c2['radius'])
    c2['angle'] = myangle
    (myangle) = revolve(c3['angle'],c3['dir'],c3['centerx'],c3['centery'],c3['speed'],c3['color'],c3['radius'])
    c3['angle'] = myangle
    (myangle) = revolve(c4['angle'],c4['dir'],c4['centerx'],c4['centery'],c4['speed'],c4['color'],c4['radius'])
    c4['angle'] = myangle
    (myangle) = revolve(c5['angle'],c5['dir'],c5['centerx'],c5['centery'],c5['speed'],c5['color'],c5['radius'])
    c5['angle'] = myangle
    (myangle) = revolve(c6['angle'],c6['dir'],c6['centerx'],c6['centery'],c6['speed'],c6['color'],c6['radius'])
    c6['angle'] = myangle
    
    CenterofMass(planetlist)
    pygame.display.update()
    time.sleep(0.02)
