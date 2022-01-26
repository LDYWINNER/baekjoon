import sys

input = sys.stdin.readline

N = int(input())
cycleNum = 0
newN = 100
while newN != N:
    if cycleNum == 0:
        newN = N
    numSum = newN // 10 + newN % 10
    newN = newN % 10 * 10 + numSum % 10
    cycleNum += 1
print(cycleNum)
