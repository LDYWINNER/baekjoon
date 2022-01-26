import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

n = str(A * B * C)
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(n)):
    count[int(n[i])] += 1

for j in count:
    print(j)
