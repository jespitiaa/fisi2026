uAst = 1.45*10**8
uTmp = 3.15*10**7
uMS = 333000
uMT = 2*10**30

class CuerpoCeleste:
    
    def __init__(self,x,y,vx,vy,m):
        self.xpos=x
        self.ypos=y
        self.vx=vx
        self.vy=vy
        self.mass=m
        self.fx=0
        self.fy=0

    def calculeFuerza(self):
        M_sun = 1
        g = 39.5
        r = ((self.xpos**2)+(self.ypos**2))**(1/2)
        self.fx = (g* self.mass * M_sun)*self.xpos/(r**3)
        self.fy = (g* self.mass * M_sun)*self.ypos/(r**3)
        
    def muevete(self,dt):
        self.vx += (self.fx/self.mass)*dt
        self.vy += (self.fy/self.mass)*dt
        self.xpos += self.vx*dt 
        self.ypos += self.vy*dt
    
    
tierra = CuerpoCeleste(1,0,0,6.28,uMS**-1)
dt = 365**-1
tactual = 0.0
while (tactual < 0.25):
    tierra.muevete(dt)
    print('t: '+str(tactual) + ', x: '+str(tierra.xpos) + ', y: ' + str(tierra.ypos))
    tactual += dt

print('posicion final: (' + str(tierra.xpos) + ','+str(tierra.ypos)+')')    
