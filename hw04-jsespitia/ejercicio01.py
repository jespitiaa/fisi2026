#coding utf-8
import sys
n = int(sys.argv[1])

def sumaRecursiva (num):
    print(num)
    if(num==1):
        return 1
    elif(num==0):
        return 0
    elif(num<0):
        print('El numero ingresado no es valido')
    else:
        return num + sumaRecursiva(num-1)

print(sumaRecursiva(n))
