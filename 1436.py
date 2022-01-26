import sys
input = sys.stdin.readline

N = int(input())

count = 0
tempNum = 0
while count < N:
    if "666" in str(tempNum):
        count += 1
    tempNum += 1

print(tempNum - 1)