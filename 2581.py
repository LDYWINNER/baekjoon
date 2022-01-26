import math
import sys

input = sys.stdin.readline

M = int(input())
N = int(input())
res = list()
n = int(math.sqrt(N)) + 1
total = 0
if M == 1:
    M = 2
for i in range(M, N + 1):
    for j in range(2, min(i, n)):
        if i % j == 0:
            break
    else:
        res.append(i)
        total += i

if len(res) > 0:
    print(total)
    print(min(res))
else:
    print(-1)
