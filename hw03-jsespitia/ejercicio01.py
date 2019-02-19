import sys


height = int(sys.argv[1])
for i in range(0, height):
    str =""
    curSp = 0
    starsRem = i + 1
    while(curSp < height - i - 1):
        str = str + " "
        curSp = curSp + 1

    while(starsRem > 0 ):
        starsRem = starsRem - 1
        str = str + "* "
    print(str)
