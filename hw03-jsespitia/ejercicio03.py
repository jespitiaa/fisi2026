import sys

path = sys.argv[1]

file = open(path, "r")
lines = file.readlines()
file.close()

nwords = []

for line in lines:
    line = line.lower()
    words = line.split()
    for word in words:
        if(word.startswith("n")):
            nwords.append(word)
print(nwords)
