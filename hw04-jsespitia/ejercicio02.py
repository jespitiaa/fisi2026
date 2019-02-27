#coding utf-8
import sys
num = int(sys.argv[1])

triangle = []
def lineaPascal(n):
    if(n==1):
        triangle.append([1])
        triangle.append([n,n])
        return [1,1]
    elif(n==0):
        triangle.insert(0,[1])
        return [1]
    elif(n<0):
        print('no existe un triangulo para '+n)
    else:
        otherList = [1]
        listaAnterior=lineaPascal(n-1)
        for i in range(0,len(listaAnterior)):
            print(i)
            if(i<len(listaAnterior)-1):
                #print(listaAnterior[i]+(listaAnterior[i+1]))
                otherList.append(listaAnterior[i]+(listaAnterior[i+1]))
            else:
                otherList.append(1)
        triangle.append(otherList)
        return otherList
lineaPascal(num)

print(triangle)
