import sys
num = int(sys.argv[1])

postes = [[],[],[]]

for i in range(1,num+1):
    postes[0].append(i)
print(postes)

def moverTorre(diameter,src,dst):
    if(diameter>postes[src][len(postes[src])-1]):
        raise Exception('Diameter > disk actual diameter')
    for i in range(0,len(postes[src])):
        if(postes[src][i]<=diameter):
            postes[dst].append(postes[src][i])
    for i in range(0,len(postes[src])):
        if(postes[src][i]<=diameter):
            
moverTorre(n-1,0,1)
print(postes)
    
    
        
