import math
import sys

input = sys.stdin.readline

M, N = map(int, input().split())

n = int(math.sqrt(N)) + 1
if M == 1:
    M = 2
for i in range(M, N + 1):
    for j in range(2, min(i, n)):
        if i % j == 0:
            break
    else:
        print(i)
