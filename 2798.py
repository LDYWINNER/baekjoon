import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
coms = list(combinations(nums, 3))

temp = []
for com in coms:
    x, y, z = com
    temp.append(x + y + z)

temp.sort()
if M in temp:
    print(M)
else:
    temp.append(M)
    temp.sort()
    print(temp[temp.index(M) - 1])
