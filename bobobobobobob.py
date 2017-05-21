GRAY = (125,125,125)
class Planet:
    def _init_(self,name,loc,mass,velocity,radius,color = GRAY):
        self.name = name
        self.loc = loc
        self.mass = mass
        self.velocity = velocity
        self.radius = radius
        self.color = color
        return
    def draw(self, surface, border = 1):
        pygame.draw.circle(surface, self.color, self.loc,self.radius,border)
    def gravity(self, loc, mass):
        force = G*mass*self.mass/((loc[0]-self.loc[0])**2+(loc[1]-self.loc[1])**2)
        ac = force/self.mass
        dpX = loc[0]-self.loc[0]
        dpY = loc[1]-self.loc[1]
        dp = sqrt(dpX**2+dpY**2)
        acX = (dpX*ac)/dp
        acY = (dpY*ac)/dp
        acvec = (acX,acY)
        
