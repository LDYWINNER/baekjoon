import sys
input = sys.stdin.readline

n = int(input())

if n == 0 or n == 1:
    print(1)
else:
    fiboList = [0, 1]
    for i in range(0, n - 1):
        fiboList.append(fiboList[i] + fiboList[i + 1])
    print(fiboList[-1])
