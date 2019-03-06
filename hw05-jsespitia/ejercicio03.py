
k = 0.0005
g = 980
class Pelota:
    
    def __init__(self,x,y,vx,vy,m):
        self.xpos = x
        self.ypos = y
        self.vx = vx
        self.vy = vy
        self.mass = m
        self.fx = 0
        self.fy = 0
    def calcularFriccion(self):
        self.fx = (k*self.mass)*(g*self.vx)
        self.fy = (k*self.mass)*(g*self.vy)
    def moverse(self,dt):
        self.xpos += self.vx*dt
        self.vx += (self.fx/self.mass)*dt
        self.ypos += self.vy*dt
        self.vy += (self.fy/self.mass)*dt
        
ball = Pelota(0,0,10,0,150)
dt = 1*10**-2
print(dt)
tactual = 0.0
posicionesX = []
tiempos = []

while (tactual<10.0):
    ball.moverse(dt)
    ball.calcularFriccion()    
    posicionesX.append(ball.xpos)
    tiempos.append(tactual)
    #print(tactual)
    tactual+=dt
    #print('tiempo ' + str(tactual)+ ' x ' + str(ball.xpos))

import matplotlib.pyplot as plt

fig = plt.figure(figsize = (5,5))
plt.plot(posicionesX,tiempos)
plt.savefig('bola.png')
print('guardado')
