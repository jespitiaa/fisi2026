import sys

num = int(sys.argv[1])
if(num == 0 or num == 1):
    print(1)
else:
    ans = 1
    for i in range (1, num+1):
        ans = ans * i
    print(ans)
