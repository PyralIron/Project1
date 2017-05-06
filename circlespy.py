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
time.sleep(0.5)
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
Ten24 = 10**24
G = 3.026757*(10**(-25))
x = 0
y = 0
def Circle(surface, color, radius, location = MIDDLE, border = 1):
    pygame.draw.circle(surface, color, location,radius,border)


c1 = {'name':"Earth",'loc':(500,310),'mass': 5.9736*(10**28), 'velocity':[-1.5,0.0]}
c2 = {'name':"Venus",'loc':(500,400),'mass': 4.87*(10**30), 'velocity':[0.0,0.0]}
c3 = {'name':"Saturn",'loc':(500,550), 'mass': 5.0*(10**28), 'velocity':[4.0,0.0]}
c4 = {'name':"Uranus",'loc':(500,800), 'mass':1.4*(10**27), 'velocity':[0.0,-1.0]}
c5 = {'name':"Jupiter",'loc':(500,452), 'mass':1900.0*(10**28), 'velocity':[0.0,0.0]}
c6 = {'name':"Sun",'loc':(500,400), 'mass':1988000.0*(10**28), 'velocity':[0.0,0.0]}
planetlist = (c1,c2,c3,c4)
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
    #print (centerOfMassX,centerOfMassY,totalMass)
    return (centerOfMassX,centerOfMassY,totalMass)
Circle(windowSurface, color, radius, location, 1)
CenterofMass(planetlist)
def gravity(planetlist):
    planetstuff = []
    i = 0
    while i < len(planetlist):
        j = 0
        planetstuff.append([[0,0],[0,0]])
        while j < len(planetlist):
            if i != j:
                force =G*planetlist[j]['mass']*planetlist[i]['mass']/((planetlist[j]['loc'][0]-planetlist[i]['loc'][0])**2+(planetlist[j]['loc'][1]-planetlist[i]['loc'][1])**2)
                accel = force/planetlist[i]['mass']
                displacementX = (planetlist[j]['loc'][0]-planetlist[i]['loc'][0])
                displacementY = (planetlist[j]['loc'][1]-planetlist[i]['loc'][1])
                displacement = sqrt(displacementX**2+displacementY**2)
                accelX = (displacementX*accel)/displacement 
                accelY = displacementY*accel/displacement
                accelVec = (accelX,accelY)
                planetstuff[i][0] = accelVec
            j += 1
        i += 1
    i = 0
    while i < len(planetlist):
        newVelX = (planetlist[i]['velocity'][0]+planetstuff[i][0][0]*0.02)
        newVelY = (planetlist[i]['velocity'][1]+planetstuff[i][0][1]*0.02)
        newVel = (newVelX,newVelY)
        #print (planetlist[i]['name'])
        #print ("accel",accelVec)

        #print ("velocity" + str(planetlist[i]['velocity'][0]) + "," + str(planetlist[i]['velocity'][1]))
        positionX = planetlist[i]['loc'][0]+newVel[0]
        positionY = planetlist[i]['loc'][1]+newVel[1]
        position = (positionX,positionY)
        
        planetlist[i]['velocity'] = newVel
        planetlist[i]['loc'] = position
        Circle(windowSurface, WHITE, 5, (floor(planetlist[i]['loc'][0]),floor(planetlist[i]['loc'][1])), 1)
        i += 1        
        
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
def velocity(i,theplanetlist,centerOfMass):
    
    force =G*centerOfMass[2]*i['mass']/((centerOfMass[0]-i['loc'][0])**2+(centerOfMass[1]-i['loc'][1])**2)
    accel = force/i['mass']
    displacementX = -(i['loc'][0]-centerOfMass[0])
    displacementY = -(i['loc'][1]-centerOfMass[1])
    displacement = sqrt(displacementX**2+displacementY**2)
    accelX = (displacementX*accel)/displacement 
    accelY = displacementY*accel/displacement
    accelVec = (accelX,accelY)
    newVelX = (i['velocity'][0]+accelVec[0]*0.02)
    newVelY = (i['velocity'][1]+accelVec[1]*0.02)
    newVel = (newVelX,newVelY)
    #print (i['name'])
    #print ("accel",accelVec)
    i['velocity'] = newVel
    #print ("velocity" + str(i['velocity'][0]) + "," + str(i['velocity'][1]))
    positionX = i['loc'][0]+newVel[0]
    positionY = i['loc'][1]+newVel[1]
    position = (positionX,positionY)
    i['loc'] = position
    #print ("position"+str(i['loc'][0]) + "," + str(i['loc'][1]))
    #print ("-------------------------------------")
    Circle(windowSurface, color, radius, (floor(i['loc'][0]),floor(i['loc'][1])), 1)
    return(i['loc'])
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(BLACK)
    gravity(planetlist)

    
    
    pygame.display.update()
    time.sleep(0.02)
