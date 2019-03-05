uAst = 1.45*10**8
uTmp = 3.15*10**7
uMS = 333000
uMT = 2*10**30
g = 6.674*10**-11

class CuerpoCeleste:
    
    def __init__(self,x,y,vx,vy,m):
        self.xpos=x
        self.ypos=y
        self.vx=vx
        self.vy=vy
        self.mass=m
        self.fx=0
        self.fy=0

    def calculeFuerza():
        #Toca revisar esto
        fmag = (g* self.mass)/((self.xpos**2)+(self.ypos**2))


    def muevete(dt):
        self.xpos = self.xpos + self.vx*dt + ((dt**2)*(self.fx/self.mass))/2
        self.ypos = self.ypos + self.vy*dt+ ((dt**2)*(self.fy/self.mass))/2
    
tierra = CuerpoCeleste(1,0,0,6.28,1/uMS)
dt = 1/365
for i in range(0,365/4):
    muevete(dt)
    print('t: '+str(dt*i) + ', x: '+str(tierra.xpos) + ', y: ' + str(tierra.ypos))
print('posicion final: ' + tierra.xpos)    