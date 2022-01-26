import math
import sys

input = sys.stdin.readline

while True:
    total = 0
    n = int(input())
    tempN = int(math.sqrt(2 * n)) + 1
    if n == 0:
        break
    if n == 1:
        print(1)
        continue
    for i in range(n + 1, 2 * n + 1):
        for j in range(2, min(i, tempN)):
            if i % j == 0:
                break
        else:
            total += 1
    print(total)
