import sys
from itertools import product

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
temp = [str(x) for x in range(1, N + 1)]
if M == 1:
    for num in temp:
        print(str(num) + "\n")
else:
    nums = [p for p in product(temp, repeat=M)]
    for num in nums:
        temp2 = list(num)
        print(" ".join(temp2) + "\n")
