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
time.sleep(0.5)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,200,50)
RED = (200,4,53)
BLUE = (0,34,200)
PURPLE = (200,0,200)
YELLOW = (200,200,0)
RAND = (160,200,30)
GRAY = (200,200,200)
location = (250,200)
radius = 5
color = WHITE
border = 5
speed = 0.1
sun = (500,400)
Ten24 = 10**24
G = 3.026757*(10**(-23))
x = 0
y = 0
planetstuff = []
windowSurface = pygame.display.set_mode(BOTTOM_R,0,32)
class Planet:
    def __init__(self,name,loc,mass,velocity,radius,color = GRAY):
        self.name = name
        self.loc = loc
        self.mass = mass
        self.velocity = velocity
        self.radius = radius
        self.color = color
        return
    def draw(self, surface, border = 1):
        pygame.draw.circle(surface, self.color, (floor(self.loc[0]),floor(self.loc[1])),self.radius,border)

def acceleration(planets, selfindex):
    targetplanet = planets[selfindex]
    global planetstuff
    planetstuff.append([0,0])
    for index, other_planet in enumerate(planets):
        if index != selfindex:
            dpX = -(targetplanet.loc[0]-other_planet.loc[0])
            dpY = -(targetplanet.loc[1]-other_planet.loc[1])
            force = G*targetplanet.mass*other_planet.mass/(dpX**2+dpY**2)
            ac = force/other_planet.mass
            dp = sqrt(dpX**2+dpY**2)
            acX = (dpX*ac)/dp
            acY = (dpY*ac)/dp
            acvec = (acX,acY)
            #print (planetstuff)
            planetstuff[selfindex][0] += acvec[0]
            planetstuff[selfindex][1] += acvec[1]
    return planetstuff[selfindex]

def calculate_position(planets):
    global planetstuff
    planetstuff = []
    planetaccel = []
    for index, target_planet in enumerate(planets):
        planetaccel.append(acceleration(planets, index))
    for index, target_planet in enumerate(planets):

        newVelX = target_planet.velocity[0]+planetaccel[index][0]*0.02
        newVelY = target_planet.velocity[1]+planetaccel[index][1]*0.02
        newVel = (newVelX,newVelY)
        positionX = target_planet.loc[0]+newVel[0]
        positionY = target_planet.loc[1]+newVel[1]
        position = (positionX,positionY)
        #print ("position"+str(position[0])+" " + str(position[1]))
        target_planet.velocity = newVel
        target_planet.loc = position

planets = [
    Planet("Earth",(500,290),5.0*(10**27),[5.0,0.5],5,RED),
    Planet("Venus",(650,300),5.0*(10**27),[0.0,2.5],5,BLUE),
    Planet("Saturn",(500,900),5.0*(10**27),[3.0,-2.0],5,PURPLE),
    Planet("Uranus",(200,100),5.0*(10**27),[4.0,2.0],5,YELLOW),
    #Planet("Jupiter",(500,452),10.0*(10**27),[0.0,0.0],5,WHITE),
    #Planet("Sun",(500,400),190.0*(10**27),[0.0,0.0],5,RAND)
    ]

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        windowSurface.fill(BLACK)
        calculate_position(planets)
        for target_planet in planets:
            target_planet.draw(windowSurface,1)

        pygame.display.update()
        time.sleep(0.02)

if __name__ == "__main__":
    main()
