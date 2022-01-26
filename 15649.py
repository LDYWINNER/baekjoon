import sys
from itertools import permutations
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
temp = [str(x) for x in range(1, N + 1)]
#print(str(temp))
if M == 1:
    for num in temp:
        print(str(num) + "\n")
else:
    combs = list(permutations(temp, M))
    for com in combs:
        temp2 = list(com)
        print(" ".join(temp2) + "\n")
