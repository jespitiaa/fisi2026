import math

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)

def serie(x,n):
    if(n==0):
        return 1
    else:
        suma = serie(x,n-1)
        if(n%2==1):
            suma = suma - x**(2*n)/fact(2*n)
        else:
            suma = suma + x**(2*n)/fact(2*n)
        return suma
print(serie(math.pi/6, 4))
print(math.cos(math.pi/6))

print('error = ' + str(math.fabs((math.cos(math.pi/6)-serie(math.pi/6, 4))*100/math.cos(math.pi/6))))
