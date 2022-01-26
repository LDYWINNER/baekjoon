import sys

input = sys.stdin.readline

N = int(input())
temp = str(input())
total = 0
for i in range(0, N):
    total += int(temp[i])
print(total)
