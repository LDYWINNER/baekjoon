import sys
input = sys.stdin.readline

n = int(input())
fiboList = [0, 1]
for i in range(0, n - 1):
    fiboList.append(fiboList[i] + fiboList[i + 1])
print(fiboList[n] % 1000000)
