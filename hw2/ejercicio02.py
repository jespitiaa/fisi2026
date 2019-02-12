a=3.1416
b="Una aproximación del valor de Pi es"
c=True
d=False
e=1
f=0

type(a) #Imprime <class 'float'>
type(b) #Imprime <class 'str'>
type(c) #Imprime <class 'bool'>
type(d) #Imprime <class 'bool'>
type(e) #Imprime <class 'int'>
type(f) #Imprime <class 'int'>

b + a #En este caso, el resultado de esta línea es un error, ya que no hay concordancia de tipos entre a y b para operar (concatenar)
#El comando funciona cuando b y a son del mismo tipo.
int(b) + int(a) #En este caso, el resultado es un error ya que no se puede conseguir un valor entero a partir del string que se inicializa en b
#El comando funciona cuando b y a se pueden convertir a entero (Algunos strings, objetos representados como byte o números).
float(b) + float(a) #En este caso, el resultado es un error ya que no se puede conseguir un valor float a partir del string en b
#El comando funciona cuando b y a se pueden convertir a float (Algunos strings o números).
str(b) + str(a) #En este caso, el resultado es un string que se obtiene a partir de la concatenación de los valores textuales de b con a.
#El comando funciona con cualquier tipo de dato que se ingrese
c + e #En este caso, el resultado es 2, puesto que el valor de verdad se toma como un número binario con valor 1
#El comando funciona si c y e tienen el mismo tipo
d | e #En este caso, el resultado es 1, pues se realiza una disyunción lógica entre un 0 y un 1
#El comando funciona cuando d y e se pueden representar de forma binaria. Fallaría con dicts
bool(a) # En este caso, el resultado es true. La función convierte cualquier valor a su valor binario. Tiene en cuenta los "vacíos" como falso (dicts vacios, arrays vacios, 0, strings vacios, False)
bool(b) # En este caso, el resultado es true. La función convierte cualquier valor a su valor binario. Tiene en cuenta los "vacíos" como falso (dicts vacios, arrays vacios, 0, strings vacios, False)
bool(f) # En este caso, el resultado es false. La función convierte cualquier valor a su valor binario. Tiene en cuenta los "vacíos" como falso (dicts vacios, arrays vacios, 0, strings vacios, False)

h={}
bool(h) #False
