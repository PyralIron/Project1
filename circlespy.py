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
time.sleep(0.5)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,200,50)
RUST = (255,69,0)
ORANGE = (255,140,0)
CORAL = (255,127,80)
TAN = (210,180,140)
RED = (200,4,53)
BLUE = (0,34,200)
CADETBLUE = (95,158,160)
PALEGOLD = (230,190,138)
PURPLE = (200,0,200)
YELLOW = (200,200,0)
RAND = (160,200,30)
AQUA = (0,150,200)
GRAY = (200,200,200)
location = (250,200)
radius = 5
color = WHITE
border = 5
speed = 0.1
sun = (500,400)
#default: 1 pix = 10^10 m
scalefactor = 10**10
G = 6.6741*(10**(-11)/(scalefactor**3))/(10**(-12))*6.91
x = 0
y = 0
F = 9.0
BasicFont = pygame.font.SysFont(None,13)
VelConv = 7.3*10**(-5)
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
            ac = force/targetplanet.mass
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
    global scalefactor
    #print (scalefactor)
    for index, target_planet in enumerate(planets):
        planetaccel.append(acceleration(planets, index))
    for index, target_planet in enumerate(planets):

        newVelX = target_planet.velocity[0]+planetaccel[index][0]
        newVelY = target_planet.velocity[1]+planetaccel[index][1]
        newVel = (newVelX,newVelY)
        positionX = target_planet.loc[0]+newVel[0]
        positionY = target_planet.loc[1]+newVel[1]
        position = (positionX,positionY)
        #print ("position"+str(position[0])+" " + str(position[1]))
        target_planet.velocity = newVel
        target_planet.loc = position

planets = [
    Planet("Sun",(500,400),1.989*(10**30),[0.0,0.0],5,YELLOW),
    Planet("Earth",(500,415.21),5.97*(10**24),[VelConv*105444.0,0.0],2,CADETBLUE),
    Planet("Mars",(500,424.923),0.642*(10**24),[VelConv*79092.0,0.0],2,RUST),
    Planet("Jupiter",(500,322.14),1898.0*(10**24),[VelConv*44784.0*(-1),0.0],2,PALEGOLD),
    Planet("Saturn",(500,551.45),568.0*(10**24),[VelConv*32724.0,0.0],2,CORAL),
    Planet("Uranus",(500,700.362),86.8*(10**24),[VelConv*23364.0,0.0],2,AQUA),
    Planet("Neptune",(500,-54.567),102.0*(10**24),[VelConv*19332.0*(-1),0.0],2,BLUE),
    Planet("Pluto",(500,1137.593),0.0146*(10**24),[VelConv*13356.0,0.0],2,TAN),
    #Planet("Comet1",(500,300),102.0*(10**20),[VelConv*17548.0,0.0],2,GREEN),
    #Planet("Comet2",(500,500),102.0*(10**20),[VelConv*17548.0,0.0],2,GREEN),
    #Planet("Comet3",(500,1000),102.0*(10**20),[VelConv*7548.0,0.0],2,GREEN),
    #Planet("Comet4",(500,900),102.0*(10**20),[VelConv*7548.0,0.0],2,GREEN),
    #Planet("Comet5",(500,1100),102.0*(10**20),[VelConv*7548.0,0.0],2,GREEN),
    #Planet("Comet6",(500,850),102.0*(10**20),[VelConv*7548.0,0.0],2,GREEN),
    #Planet("Comet7",(500,750),102.0*(10**20),[VelConv*7548.0,0.0],2,GREEN),
    #Planet("Comet8",(500,650),102.0*(10**20),[VelConv*17548.0,0.0],2,GREEN),
    #Planet("Comet9",(500,200),102.0*(10**20),[VelConv*17548.0,0.0],2,GREEN),
#Balanced Orbits
    #Planet("Body1",(500,600),10.0*(10**30),[1.0,0.0],5,YELLOW),
    #Planet("Body2",(500,200),10.0*(10**30),[-1.0,0.0],5,BLUE),
    #Planet("Body3",(700,400),10.0*(10**24),[0.0,-3.0],5,RED),
    #Planet("Body4",(300,400),10.0*(10**24),[0.0,3.0],5,GREEN),
    #Planet("Body5",(500,50),10.0*(10**24),[-6.5,0.0],2,ORANGE),
    #Planet("Body6",(500,750),10.0*(10**24),[6.5,0.0],2,AQUA),
    #Planet("Body5",(500,400),10.0*(10**29),[0.0,0.0],5,AQUA)
    ]
def rendertext(body):
    bodyname = BasicFont.render(body.name,True,WHITE,BLUE)
    bodynameRect = bodyname.get_rect()
    bodynameRect.centerx = body.loc[0]
    bodynameRect.centery = body.loc[1]+10
    windowSurface.blit(bodyname,bodynameRect)
def renderall(planets):
    for planet in planets:
        rendertext(planet)
def scalepos(planets, zoom):
    for planet in planets:
        planet.loc[0] = zoom*planet.loc[0]
def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_d:
                    print("h")
                    pygame.transform.scale(windowSurface, (1000,800))
            if event.type == MOUSEMOTION:
                mousepos = pygame.mouse.get_pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    #print ("4")
                    #dialation by factor 1/2 centered on cursor
                    global scalefactor
                    scalefactor *= 1.125
                    #print (scalefactor)
                    global G
                    G = 6.6741*(10**(-11)/(scalefactor**3))/(10**(-12))*6.91
                    for planet in planets:
                        #print (planet.loc)
                        newloc = (1/1.125*(planet.loc[0]-500)+500,1/1.125*(planet.loc[1]-400)+400)
                        planet.loc = newloc
                        newvel = (1/1.125*planet.velocity[0],1/1.125*planet.velocity[1])
                        planet.velocity = newvel
                elif event.button == 5:
                    #print ("5")
                    scalefactor /= 1.125
                    for planet in planets:
                        newloc = (1.125*(planet.loc[0]-500)+500,1.125*(planet.loc[1]-400)+400)
                        planet.loc = newloc
                        newvel = (1.125*planet.velocity[0],1.125*planet.velocity[1])
                        planet.velocity = newvel
                    global scalefactor
                    #print (scalefactor)
                    global G
                    G = 6.6741*(10**(-11)/(scalefactor**3))/(10**(-12))*6.91
        windowSurface.fill(BLACK)
        calculate_position(planets)
        for target_planet in planets:
            target_planet.draw(windowSurface,1)
            rendertext(target_planet)

        pygame.display.update()
        time.sleep(0.01)

if __name__ == "__main__":
    main()
