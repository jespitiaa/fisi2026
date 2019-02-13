
import sys

year = int(sys.argv[1])
if(not(year%4 and year%100 and year%400)):
    print(str(year)+" es bisiesto")
else:
    print(str(year)+" no es bisiesto")
